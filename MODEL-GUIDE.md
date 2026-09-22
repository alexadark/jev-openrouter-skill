# Jev Model Guide

> A bounded decision adviser for Codex. Jev recommends a model profile. It does not perform the task, change the active model, or route work automatically.

**Grid date:** 2026-09-22  
**Runtime:** Codex-only v1  
**Decision order:** reliability first, avoidable interventions second, total cost third

## The three systems stay separate

| Layer | Role | Consumption |
| --- | --- | --- |
| Codex | Runs the skill and, after your manual choice, can perform the task | Native OpenAI models remain on your Codex subscription |
| Jev through OpenRouter | Makes one structured recommendation from the allowed profiles | OpenRouter usage |
| DeepSeek V4.1 Flash | Optional execution model only when eligible and manually selected | Ollama Cloud, consumed separately |

There is no automatic switch. After reading the recommendation, you choose the model and effort manually in Codex.

## Model grid

The grid is a practical policy, not a promise of model performance. High and XHigh are justified by an identified reasoning difficulty, not by importance or duration alone.

| Profile | Best fit | Boundary |
| --- | --- | --- |
| **Luna Low** | Short translation, titles, simple reformulation, exact extraction, classification, targeted lookup | Low ambiguity, easy verification, no sensitive architecture or product decision |
| **Luna Medium** | Bounded inventory, constrained extraction, small known-cause fix with a clear test | Mechanical work can be long without needing a larger model |
| **Luna High** | Substantial bounded implementation, stable contracts, multi-step logic, observable tests | Not the default owner of a long unsupervised integration chain |
| **Luna XHigh** | Bounded work with a concrete reasoning problem that High did not resolve | Exceptional, never the default for extraction, inventory, or routine tests |
| **Sol Medium** | Faithful synthesis, meeting preparation, polished writing, scoped comparison, everyday development | First candidate for prolonged, well-specified work with stable contracts and strong automated checks |
| **Sol High** | Sol-level work with specific nested constraints or contradictions that Medium may miss | Not a generic reliability upgrade for every long task |
| **Astra Medium** | Dependent long runs, multiple tools or components, expensive late errors, architecture, ambiguous diagnosis, complex planning | May be selected directly when the dependency risk is real; no smaller-model failure ritual is required |
| **Astra High** | Precisely identified critical difficulty not resolved at Medium, or clearly requiring deeper analysis | Use for one bounded pass, then return to Medium after resolving it |
| **Astra XHigh** | Exceptional complexity with a documented High-level impasse or equivalent evidence | Never automatic for a large phase, long document, or important request |
| **DeepSeek Low** | Conditional: bounded classification, data transformation, or drafting from supplied excerpts | Ollama Cloud must be available, data must be eligible, and preserving Codex quota or a favorable local comparison must matter |
| **DeepSeek High** | Conditional: synthesis of selected excerpts, test proposals, or an isolated fix with a clear contract and validation | Not the default for a long, dependent, autonomous run; Max benchmark results do not prove High behavior |

## Ask Jev

### OpenAI only

```text
Use $jev-openrouter to recommend the model and reasoning effort for:
Summarize a 90-minute customer interview into themes, evidence, risks, and next actions.
Use OpenAI profiles only.
Do not start the task.
```

### Consider DeepSeek

```text
Use $jev-openrouter to recommend the model and reasoning effort for:
Classify 400 public product reviews into an existing taxonomy and return schema-valid JSON.
Ollama Cloud is available, these public reviews may be sent there, and preserving Codex quota matters. Consider DeepSeek as well as OpenAI.
Do not start the task.
```

## What a useful answer looks like

```text
Recommendation: gpt-5.6-sol, Medium

Why: The task requires faithful synthesis and prioritization, but its sources,
output structure, and validation criteria are already bounded.

Re-evaluate if: contradictions across sources become material or the work expands
into a dependent multi-system implementation.

Jev choice: sol_medium, 0.62 among the supplied options
Decision model: shown only if returned by OpenRouter
Cost: shown only if returned by OpenRouter

Manual next step: select Sol and Medium in Codex if you accept the recommendation.
```

The probability is Jev's distribution across the choices it received. It is not a 62 percent chance of success. The example is illustrative, not a live Jev result or a performance claim.

## Data and constraint warning

Jev receives only the state needed to make the decision. Do not send a repository, vault, transcript, customer record, or conversation history by default. Summarize the task and disclose only the constraints needed for model selection.

An OpenAI-only constraint excludes DeepSeek. A strictly local-data constraint excludes every cloud profile in this grid, including OpenAI and DeepSeek. If no profile is admissible, the skill should say so rather than export data or invent an option.

Tools, permissions, missing sources, and unclear acceptance criteria are not solved by more reasoning effort. Fix the constraint or state the assumption first.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Codex does not recognize `$jev-openrouter` | Confirm the repository is at `~/.agents/skills/jev-openrouter`, then start a fresh Codex session |
| `OPENROUTER_API_KEY is not available` | Export the variable in the environment that launches Codex; never place the value in the repository |
| OpenRouter rejects the request | The Decisions endpoint is alpha and its contract may have changed; review the current OpenRouter and TypeSafe documentation |
| DeepSeek is absent | It was filtered out by an OpenAI-only or data rule, or Ollama Cloud availability was not established |
| The answer feels overpowered | Check whether the prompt named a real reasoning difficulty, dependent steps, weak validation, or expensive late errors |
| Only one profile is allowed | The restriction already decides the choice; a Jev call adds no useful comparison |
| No model or cost is shown for Jev | Report those fields only when OpenRouter returns them; do not infer or invent them |

## Installation

```bash
npx skills add alexadark/jev-openrouter-skill --skill jev-openrouter
```

Manual fallback:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/alexadark/jev-openrouter-skill ~/.agents/skills/jev-openrouter
```

Set `OPENROUTER_API_KEY` securely, start Codex fresh, and invoke the skill explicitly. See the [README](README.md) for the short setup path or open the [standalone handbook](index.html) for the complete visual guide.
