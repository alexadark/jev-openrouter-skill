#!/usr/bin/env python3
"""Call TypeSafe Jev through OpenRouter's Decisions API."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

DEFAULT_ENDPOINT = "https://openrouter.ai/api/alpha/decisions"
DEFAULT_MODEL = "~typesafe/jev-latest"
ALLOWED_FIELDS = {"model", "state", "questions", "provider", "trace", "session_id", "user"}


def fail(message: str, code: int = 2) -> None:
    print(f"jev-openrouter: {message}", file=sys.stderr)
    raise SystemExit(code)


def load_request(path: str) -> dict[str, Any]:
    try:
        if path == "-":
            value = json.load(sys.stdin)
        else:
            with Path(path).expanduser().open(encoding="utf-8") as handle:
                value = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"could not read request JSON: {exc}")

    if not isinstance(value, dict):
        fail("request must be a JSON object")
    return value


def validate_question(question_id: str, question: Any) -> None:
    if not isinstance(question, dict):
        fail(f"question {question_id!r} must be an object")
    kind = question.get("type")
    if kind not in {"choice", "noul", "score"}:
        fail(f"question {question_id!r} has unsupported type {kind!r}")
    if not isinstance(question.get("instructions"), str) or not question["instructions"].strip():
        fail(f"question {question_id!r} needs non-empty instructions")

    criteria = question.get("criteria")
    if kind == "choice":
        if not isinstance(criteria, dict) or len(criteria) < 2:
            fail(f"choice question {question_id!r} needs at least two criteria options")
    elif kind == "score":
        if not isinstance(criteria, list) or len(criteria) < 2 or any(item is None for item in criteria):
            fail(f"score question {question_id!r} needs at least two non-null criteria levels")
    elif criteria is not None:
        if not isinstance(criteria, dict) or not {"true", "false"}.issubset(criteria):
            fail(f"noul question {question_id!r} criteria must describe both true and false")


def normalize_request(raw: dict[str, Any], model_override: str | None) -> dict[str, Any]:
    unknown = sorted(set(raw) - ALLOWED_FIELDS)
    if unknown:
        fail(f"unsupported top-level fields: {', '.join(unknown)}")

    if "state" not in raw:
        fail("request needs a state")
    if not isinstance(raw["state"], (str, dict, list)):
        fail("state must be a string, object, or array")

    questions = raw.get("questions")
    if not isinstance(questions, dict) or not questions:
        fail("request needs a non-empty questions object")
    for question_id, question in questions.items():
        validate_question(str(question_id), question)

    payload = dict(raw)
    payload["model"] = model_override or payload.get("model") or DEFAULT_MODEL
    if not isinstance(payload["model"], str) or not payload["model"].strip():
        fail("model must be a non-empty string")
    return payload


def call_jev(payload: dict[str, Any], endpoint: str, timeout: float) -> dict[str, Any]:
    api_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not api_key:
        fail("OPENROUTER_API_KEY is not available", code=1)

    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload, separators=(",", ":")).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "codex-jev-openrouter/1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        fail(f"OpenRouter returned HTTP {exc.code}: {body}", code=1)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        fail(f"OpenRouter request failed: {exc}", code=1)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request-file", default="-", help="JSON request file, or - for stdin")
    parser.add_argument("--model", help=f"override the model (default: {DEFAULT_MODEL})")
    parser.add_argument("--endpoint", default=os.environ.get("OPENROUTER_DECISIONS_URL", DEFAULT_ENDPOINT))
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--dry-run", action="store_true", help="validate and print the payload without sending it")
    args = parser.parse_args()

    payload = normalize_request(load_request(args.request_file), args.model)
    result = payload if args.dry_run else call_jev(payload, args.endpoint, args.timeout)
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2, sort_keys=True)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
