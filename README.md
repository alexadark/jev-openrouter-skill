# Jev Model Guide

Jev Model Guide is a Codex skill for one bounded decision: recommend a model and reasoning effort for a described task. It asks TypeSafe Jev through OpenRouter for a structured judgment, then returns the recommendation without starting the task or changing your active model.

This first public release supports Codex only.

## What it does

- Compares a dated, explicit set of OpenAI profiles.
- Includes Claude Opus 5.5 when Anthropic execution is allowed; see the [sourced assessment](references/claude-opus-5-5.md).
- Can consider DeepSeek V4.1 Flash through Ollama Cloud when you allow it.
- Prioritizes end-to-end reliability, then fewer avoidable interventions, then total cost.
- Keeps Jev's structured choice separate from Codex's explanation.

It does not route work automatically. Native OpenAI models continue through your Codex subscription. The Jev consultation uses OpenRouter. Claude execution requires Claude Code or a verified Anthropic-compatible runtime and separate access. DeepSeek, if you later select it, uses Ollama Cloud and separate consumption.

## Install

Prerequisites:

- Codex
- Git
- An OpenRouter API key with access to the alpha Decisions endpoint

Use the agent skill installer:

```bash
npx skills add alexadark/jev-openrouter-skill --skill jev-openrouter
```

If you prefer a manual install, clone the entire public repository into the Codex skills directory:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/alexadark/jev-openrouter-skill ~/.agents/skills/jev-openrouter
```

Set `OPENROUTER_API_KEY` through your shell, password manager, or secret manager. Do not paste a key into the skill files or commit it to Git. For a temporary terminal session without putting the value in shell history:

```bash
read -s "OPENROUTER_API_KEY?OpenRouter API key: "
export OPENROUTER_API_KEY
```

Start Codex fresh from that environment so it discovers the skill and receives the variable.

## Use

Invoke the skill explicitly and tell it not to begin the described work:

```text
Use $jev-openrouter to recommend the model and reasoning effort for:
Prepare a faithful executive synthesis of six interview transcripts.
Do not start the task.
```

For OpenAI-only advice, say so. To make DeepSeek eligible, state that Ollama Cloud is available, the data can be sent there, and you want it considered.

The OpenRouter Decisions endpoint is alpha. Returned probabilities describe Jev's preference among the supplied choices. They are not success rates. The response identifies Jev's decision model only when OpenRouter returns that field.

## Optional shared RIFF catalog

Standalone use works with the bundled, versioned catalog snapshot. To keep a personal RIFF installation and this skill on the same live policy, explicitly set `RIFF_MODEL_CATALOG` or create `~/.config/jev-openrouter/catalog.json` with `{"catalogPath":"/path/to/riff-codex/riff/references/model-profiles.json"}`. The path is local configuration, not part of this public skill. A configured missing or invalid source fails clearly instead of silently using an old release snapshot.

Inspect the effective source with `python3 <skill-directory>/scripts/model_catalog.py --source`. Read the [catalog loading contract](references/openai-model-advice.md) for precedence and privacy rules. Do not edit the generated snapshot as a separate policy; refresh it from the canonical RIFF catalog when preparing a release. No network fetch or installation happens when reading a catalog.

## Read next

- [Model guide](MODEL-GUIDE.md)
- [Standalone handbook](index.html)
- [MIT License](LICENSE)

The model grid was updated on 2026-09-24 for Claude Opus 5.5. Treat it as a dated decision policy, not a universal benchmark.
