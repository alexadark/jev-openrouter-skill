# OpenAI and DeepSeek model advice for Jev

Version: 2026-09-22. This is a proposed operating policy based on research available on that date, not a locally validated benchmark or universal ranking. It selects the primary model and reasoning effort for code and non-code work. It does not authorize automatic routing or replace an execution framework's controls.

## Priority and separate decision axes

Prioritize a correct end-to-end result, then fewer avoidable human interventions, especially during long unattended runs. Optimize total cost only after those goals. Do not invent a success rate.

Describe these axes separately in the state sent to Jev:

- **Reasoning difficulty:** known transformation, interactions to understand, or ambiguous diagnosis and planning.
- **Step dependency:** independent verifiable items versus a chain in which an early error propagates; include likely context recovery.
- **Autonomy and detectability:** supervised or unattended execution; strong automatic tests versus defects visible only at the end.
- **Late-error cost:** reversible local correction, cross-component regression, data inconsistency, or costly rework.

Duration alone does not select the model. Five hundred independent schema-validated transformations can remain Luna work. An ordinary feature that connects data, permissions, UI, and journey validation without supervision can justify Astra even when no algorithm is difficult.

## Profiles to send in `criteria`

Each row defines one `choice` option. Use Profile as the key and send the model, effort, use, and limitations together as its value. Profile keys are internal identifiers, not model API names.

| Profile | Model | Effort | Use and limitations |
| --- | --- | --- | --- |
| luna_low | gpt-5.6-luna | low | Short translation, titles, simple rewriting, classification, exact extraction, or a targeted lookup of a known file. Low ambiguity and easy verification. No architecture or sensitive judgment. |
| luna_medium | gpt-5.6-luna | medium | Bounded inventory, extraction with several constraints, or a small fix with a known cause and clear test. A long input does not require a larger model when the work remains mechanical. |
| luna_high | gpt-5.6-luna | high | Substantial bounded implementation with stable contracts, multi-step logic, and observable tests. Suitable for a verifiable unit, not the default owner of a long unattended integration chain. No open product, permission, or architecture decisions. |
| luna_xhigh | gpt-5.6-luna | xhigh | The same bounded scope with a concrete reasoning difficulty unresolved at High or equivalently demonstrated. An exception, not the default for extraction, inventories, or testing. |
| sol_medium | gpt-5.6-sol | medium | Faithful synthesis, meeting preparation, polished writing, bounded comparative research, or routine development. First candidate for prolonged, well-specified work with stable contracts, bounded steps, and strong automatic checks. Prefer Astra Medium when dependencies, context recovery, or late errors make supervision expensive. |
| sol_high | gpt-5.6-sol | high | Sol-level work with nested constraints or a specific contradiction Medium may mishandle. Not an automatic reliability premium for every long task. When the main risk is cross-step drift or coordination, consider Astra Medium instead. |
| astra_medium | gpt-6-astra | medium | First candidate for a long autonomous run with dependent steps, several tools or components, context recovery, or costly late errors, even when the code is ordinary. Also architecture, ambiguous diagnosis, complex planning, strategy, and demanding visual acceptance. It may be selected directly; do not require a smaller model to fail first. Expected benefit must be tested in the real workflow. |
| astra_high | gpt-6-astra | high | A precisely identified critical difficulty unresolved at Medium or otherwise clearly deserving deeper analysis. One bounded pass, then return to Medium. |
| astra_xhigh | gpt-6-astra | xhigh | Exceptional complexity with a documented impasse at High or equivalent justification. Not automatic for a large phase, long document, or important request. |
| deepseek_low | deepseek-v4.1-flash:cloud | low | Conditional Ollama Cloud option for classification, data transformation, or drafting from supplied excerpts when work is bounded and easy to verify. Consider to preserve Codex quota or after a favorable local comparison. Not a systematic Luna replacement or an invitation to explore a repository freely. |
| deepseek_high | deepseek-v4.1-flash:cloud | high | Conditional Ollama Cloud option for selected-source synthesis, test proposals, or an isolated fix with an explicit contract and verifier. Consider to preserve Codex quota or after favorable local evidence. Not the default for a long dependent autonomous run. Max benchmarks do not establish this High profile's performance. |

Terra, GLM, other models, Fast, Max, and Ultra are outside this initial grid. That is a scope restriction, not a claim of inferiority. Research before expanding the grid; never substitute an unlisted profile silently.

## DeepSeek eligibility and default choice

OpenAI remains the default to minimize provider changes and supervision: Luna for bounded units, Sol for well-specified routine work, and Astra for dependent long runs and difficult diagnosis. DeepSeek expands the options; it is not an automatic fallback when OpenAI quota is low.

Before including DeepSeek, check the request's provider restrictions, current availability of `deepseek-v4.1-flash:cloud` through Ollama, and whether the data may go to that cloud. “OpenAI only” excludes it. “Strictly local data” excludes every cloud profile and the Jev call itself. Advice does not authorize later transmission of a repository, vault, or history.

The local catalogue inspected on 2026-09-22 exposed `none`, `low`, `high`, and `max` for this slug, but not `medium` or `xhigh`. This grid keeps Low and High only. A catalogue entry proves neither task performance nor account availability.

DeepSeek may be the primary recommendation for an eligible bounded task when there is a concrete objective such as preserving Codex quota or reproducing a favorable local result at equal quality. Otherwise prefer OpenAI. Do not turn low API pricing into a savings claim for someone who already has Codex access; include Ollama consumption and retries.

## Decision rules to include in `state`

- Rank end-to-end correctness first, avoidable human intervention second, and total cost and duration third. Necessary approvals and real access blockers are not avoidable interventions.
- Consider work type, ambiguity, connected systems, error cost, available verification, and observed failures. Prompt length and repository size are insufficient classifiers.
- Separate faithful transformation from interpretive synthesis. Exact quotation extraction can be Luna; reconciling contradictory sources is more likely Sol or Astra.
- More reasoning does not repair missing tools, permissions, or sources. Report them.
- Do not confuse reasoning budget with endurance. High and XHigh require an identified reasoning difficulty. Long execution also depends on durable state, error detection, bounded steps, journey tests, and evidence-based recovery.
- Select the profile that performs the task, not an expensive orchestrator plus worker for a simple request.
- Minimize irrelevant context. Do not confuse API pricing, credits, and subscription quota.
- Honor explicit model constraints and current runtime capabilities. Unknown availability makes a recommendation conditional.
- When several profiles fit, choose the cheaper one only when expected reliability remains sufficient. Jev probabilities are not calibrated success rates.

## Validation examples

- Three titles from one supplied paragraph: `luna_low` candidate.
- Transform known data under an explicit schema and tests: `luna_medium` or `luna_high` depending on logic.
- Synthesize a transcript while selecting and prioritizing ideas: `sol_medium` candidate.
- Diagnose an unknown inconsistency across authentication, billing, and database: `astra_medium` candidate.
- Build several CRUD screens with stable contracts and tests: `sol_medium` candidate.
- Deliver one ordinary feature across data, permissions, UI, and integration during a long unattended run: `astra_medium` candidate.
- Classify public excerpts while preserving Codex quota and with Ollama Cloud allowed: `deepseek_low` is eligible.
- Propose tests for an isolated public function under the same quota goal: `deepseek_high` is eligible. OpenAI-only or strictly local restrictions exclude it before the Jev call.

These examples check policy coherence; they are not mandatory answers regardless of task constraints.

## Sources and refresh policy

Sources consulted on 2026-09-22:

- [OpenAI model catalogue](https://developers.openai.com/api/docs/models) and [Luna](https://developers.openai.com/api/docs/models/gpt-5.6-luna) for identifiers and capabilities. The Codex app catalogue may differ from the API.
- [Artificial Analysis on Luna](https://artificialanalysis.ai/models/releases/gpt-5-6-luna), [Sol](https://artificialanalysis.ai/models/releases/gpt-5-6-sol), and [Astra](https://artificialanalysis.ai/models/releases/gpt-6-astra) for effort tradeoffs; results depend on benchmark version.
- [Artificial Analysis on Astra](https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra) for agentic strengths and limitations.
- [Codex pricing](https://learn.chatgpt.com/docs/pricing) for consumption factors beyond message count.
- [METR task-completion time horizons](https://metr.org/time-horizons/) for dependent work and reliability distinctions; it does not directly rank these models.
- [Anthropic on long-running agent harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) for incremental work, durable state, and tests; it is not comparative OpenAI evidence.
- [Ollama DeepSeek V4.1 Flash](https://ollama.com/library/deepseek-v4.1-flash) and [desktop integration](https://docs.ollama.com/integrations/chatgpt) for the cloud slug and provider separation.
- [Artificial Analysis DeepSeek V4.1 Flash Max](https://artificialanalysis.ai/models/deepseek-v4-1-flash) for encouraging independent results and high output volume. Max and provider-specific speed do not validate Low or High through Ollama in this workflow.

Do not redo the complete research for every recommendation. Refresh relevant sources when the request is about current performance, a new model, or an unavailable profile. Jev must not invent missing benchmarks.
