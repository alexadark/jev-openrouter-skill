# Shared OpenAI and DeepSeek model catalog

Read the complete JSON returned by `python3 <skill-directory>/scripts/model_catalog.py` before giving model advice. It contains the version, objective, complete profile definitions, decision rules and research sources. This reference is a loading contract, not a second editable model grid.

## Source ownership and portability

The canonical source is RIFF's `riff/references/model-profiles.json`. The bundled [model-profiles.json](model-profiles.json) is a generated, versioned distribution snapshot of that source, not an independently maintained policy. Updating a release means replacing the snapshot from the canonical source and checking equality; do not edit two grids separately. Standalone installations require neither RIFF nor a personal path.

An installation can explicitly use the live RIFF catalog through `RIFF_MODEL_CATALOG`, `--catalog PATH`, or a local `~/.config/jev-openrouter/catalog.json` containing `{"catalogPath":"/path/to/riff-codex/riff/references/model-profiles.json"}`. The helper selects an explicit CLI path first, then the environment override, then the local configuration, otherwise the bundled snapshot. `--source` reports the selected path without a network call. An explicitly configured missing or invalid source is an error, never a silent fallback to the bundled release.

## Prepare a recommendation

Include the selected catalog's `version`, `status`, `objective` and complete `rules` in Jev's `state`, together with the smallest useful task summary. Build `criteria` from admissible profiles: `id` is the key; combine `model`, `effort`, `provider` and complete `usage` as its value. Profile ids are not model API names.

Keep reasoning difficulty, dependent steps, autonomy, verification and late-error cost separate. The catalog's priority is end-to-end correctness, then fewer avoidable interventions, then total consumption. It remains a dated operating hypothesis, not a local benchmark or universal ranking.

Filter before sending: explicit OpenAI-only excludes DeepSeek; strictly local data excludes all these cloud profiles and the Jev call for that data. DeepSeek requires checked Ollama Cloud availability, data admissibility and a concrete quota or locally demonstrated benefit. Unknown availability is not proof of support. Zero profiles means report incompatibility; one means explain the constrained choice without a redundant call.

Advice never starts the described work, switches the model, authorizes data export for later execution, changes RIFF or installs an orchestrator. Explain the actual selected profile separately from Jev's raw probabilities; they are not success rates. Other explicitly requested Jev decisions do not need this catalog.
