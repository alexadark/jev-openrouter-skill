#!/usr/bin/env python3
"""Read a shared RIFF catalog or its portable release snapshot, without network."""

import argparse
import json
import os
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", help="Explicit catalog path; invalid sources never fall back")
    parser.add_argument("--source", action="store_true", help="Print the selected source path only")
    args = parser.parse_args()
    source = None
    try:
        selected = args.catalog if args.catalog is not None else os.environ.get("RIFF_MODEL_CATALOG")
        config = Path.home() / ".config" / "jev-openrouter" / "catalog.json"
        if selected is None and config.exists():
            settings = json.loads(config.read_text(encoding="utf-8"))
            if not isinstance(settings, dict) or set(settings) != {"catalogPath"}:
                raise ValueError("invalid catalog configuration")
            selected = settings["catalogPath"]
        if selected is None:
            source = Path(__file__).resolve().parent.parent / "references" / "model-profiles.json"
        else:
            if not isinstance(selected, str) or not selected.strip():
                raise ValueError("invalid catalog path")
            source = Path(selected).expanduser()
        catalog = json.loads(source.read_text(encoding="utf-8"))
        if not isinstance(catalog, dict) or not all(catalog.get(k) for k in ("version", "objective", "rules", "profiles")):
            raise ValueError("missing catalog fields")
        if not isinstance(catalog["rules"], list) or not all(isinstance(r, str) and r.strip() for r in catalog["rules"]):
            raise ValueError("invalid rules")
        profiles = catalog["profiles"]
        if not isinstance(profiles, list) or not profiles:
            raise ValueError("invalid profiles")
        seen = set()
        for profile in profiles:
            if not isinstance(profile, dict) or not all(isinstance(profile.get(k), str) and profile[k].strip() for k in ("id", "model", "effort", "provider", "usage")):
                raise ValueError("incomplete profile")
            if profile["id"] in seen:
                raise ValueError("duplicate profile")
            seen.add(profile["id"])
    except (OSError, ValueError, TypeError) as exc:
        print(f"jev-openrouter: catalog unavailable or invalid ({type(exc).__name__}); check the explicit source or local configuration", file=sys.stderr)
        return 1
    if args.source:
        print(source.resolve())
    else:
        json.dump(catalog, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
