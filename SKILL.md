---
name: jev-openrouter
description: Invoke TypeSafe Jev through OpenRouter for an explicitly requested structured judgment, including model and reasoning-effort advice among OpenAI models and conditional DeepSeek via Ollama. Use only when the user explicitly asks for Jev or TypeSafe; do not trigger for ordinary model questions, prose or code generation, or implicit routing.
---

# Invoke Jev through OpenRouter

Keep the current Codex model as the working agent. Use Jev only for a bounded structured judgment. Reply in the user's language.

## Recommend a primary model

When the user asks Jev which model and reasoning effort to use, read the complete [OpenAI and DeepSeek model grid](references/openai-model-advice.md). This mode returns advice only: do not begin the described task, delegate it, change configuration, or switch the active model.

- Use the supplied task description and collect only constraints that materially affect the choice. Do not explore the project to perform the task while supposedly evaluating it. Ask one focused question only when the missing fact could change the recommendation; otherwise state the assumption.
- Send Jev the grid, decision rules, and every admissible profile, not just model names. Build one `choice` question named `recommended_profile`. Its `criteria` must map each profile identifier to the complete model, effort, use, and limitation text. Put the task, constraints, unknowns, grid date, and decision rules in `state`. Separately describe reasoning difficulty, dependent steps, desired autonomy, available verification, and the cost of a late error. Jev cannot see the surrounding conversation.
- Optimize first for a correct end-to-end result, then for fewer avoidable human interventions, then for total cost including retries and verification. A simple but long dependent task is not automatically a Luna task. XHigh is not a reliability guarantee.
- Preserve explicit model and provider restrictions. Filter profiles before the call. “OpenAI only” excludes DeepSeek. Strictly local data excludes every cloud profile and the Jev call itself. If one profile remains, explain the constrained choice without a redundant paid call. If none remain, report the incompatibility.
- OpenAI is the default. DeepSeek is conditional under the grid's eligibility rules. If its availability or data destination is uncertain, keep the main recommendation on an allowed OpenAI profile and name DeepSeek only as an alternative to verify. Do not send the uncertain data to it.
- Make a real script call when the user says to use Jev. Never present `--dry-run`, the working model's opinion, or a fallback as Jev's answer. Returned probabilities describe Jev's choice distribution; they are not success rates or savings percentages.
- Report the recommended primary model and effort, a short grid-based interpretation, and one concrete reason to reconsider. For a long run, also state the main drift risk and the most useful automated control. Keep Codex's interpretation separate from Jev's structured answer. Report the returned Jev model and cost only when present.
- Remind the user that changing the Codex model remains manual. Native OpenAI models continue through the user's Codex access. Jev uses OpenRouter. Conditional DeepSeek use goes through Ollama Cloud with separate consumption; do not call it local or included in Codex.

Positive examples: “Use Jev to choose the primary model for summarizing this transcript”; “Ask Jev which model and effort should diagnose this multi-service bug.”

Near misses: “Which model should I use?” without requesting Jev; “Summarize this transcript”; requests to edit or explain this skill. Handle those normally and do not call Jev.

## Design other decisions

Translate any other explicitly requested Jev decision into the smallest useful Decisions request:

- `state`: only facts needed for the decision. Do not send the whole conversation, repository, or vault.
- `questions`: one or more independent typed judgments over that state.
- `choice`: select one option from a criteria object and return probabilities.
- `noul`: estimate whether a statement is true as a probability from 0 to 1.
- `score`: locate the state on an ordered rubric with at least two concrete levels.

Keep exact rules, calculations, permissions, and actions in Codex or deterministic code. Jev supplies judgment, not authorization or generated prose.

## Invoke

Resolve this installed skill's directory, then build a JSON object with `state` and `questions` and pass it on standard input or with `--request-file`:

```bash
python3 <skill-directory>/scripts/jev_decide.py --request-file request.json
```

The script reads `OPENROUTER_API_KEY`, defaults to `~typesafe/jev-latest`, calls `https://openrouter.ai/api/alpha/decisions`, and prints the full JSON response. `--dry-run` validates and prints the outgoing payload without sending it.

Report the selected answer, relevant probabilities or score, response model, and reported cost. If the endpoint fails or returns material uncertainty, show that result instead of silently substituting another model.

The OpenRouter Decisions endpoint is alpha. If its contract changes, consult the current [TypeSafe agent documentation](https://docs.typesafe.ai/agent-skill) and [OpenRouter Jev example](https://openrouter.ai/labs/jev/compile) before changing the wrapper.
