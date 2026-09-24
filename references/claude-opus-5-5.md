# Claude Opus 5.5 assessment

Research checked on 2026-09-24. This is a sourced routing hypothesis, not a local performance benchmark. The effective profiles remain in the shared catalog.

## Verified facts

Anthropic released Opus 5.5 on September 22, 2026 for coding and knowledge work. The model ID is `claude-opus-5-5`. Its documented context window is 1M tokens, with up to 128K output tokens. Standard API pricing is $4 per million input tokens and $20 per million output tokens; cache reads cost $0.20 per million tokens. These are API prices, not subscription quota equivalents. See the [model specification](https://platform.claude.com/docs/en/models/opus-5-5/overview).

The API supports `low`, `medium`, `high`, `xhigh` and `max`; Medium is the default. Adaptive thinking stays enabled. Effort names are provider-specific and do not establish equivalence with OpenAI effort levels. See [effort documentation](https://platform.claude.com/docs/en/build-with-claude/effort).

Anthropic reports improvements in coding and complex work relative to Opus 5 and performance near Fable 5.1 on much work. These are vendor results, not evidence of superiority over Sol or Astra on this user's workflows. See the [release announcement](https://www.anthropic.com/claude-opus-5-5).

## Selection interpretation

Consider Medium alongside Sol for well-defined implementation and synthesis, and alongside Astra for long dependent coding or tool-based work. Compare completion quality, interventions, retries, elapsed time and actual consumption in the intended runtime. A larger context window alone is not a reason to select it.

Low is a bounded-work option. High, XHigh and Max require increasing, concrete reasoning justification. Do not transfer older Opus effort settings automatically or infer lower-effort results from a higher-effort benchmark.

Use Claude Code or a verified Anthropic-compatible runtime. Check model and effort availability there; a catalog entry does not prove account access or native Codex support. Claude access and consumption are separate from Codex. See [Claude Code model configuration](https://support.claude.com/en/articles/11940350-claude-code-model-configuration).

OpenAI-only excludes Claude. Local-only excludes the cloud execution profiles and sending private task data to Jev. Unknown Claude access means an alternative to verify, not permission to switch or export task data. RIFF retains its default OpenAI-only provider filter; explicitly allow `anthropic` to include these profiles there.

## Independent comparisons and early feedback

[Artificial Analysis, September 22](https://artificialanalysis.ai/articles/claude-opus-5-5/) reports parity with Astra on its terminal and automation evaluations and a lead in professional knowledge work, including presentation ahead of Sol. Its Intelligence Index gives Opus 58 at Max. However, Max produced about 119K output tokens per task versus 27K for Astra Max. Effort and harness matter; these results do not establish Medium-level parity or subscription endurance. Its evaluations used the default fallback.

[CodeRabbit's own evaluation](https://www.coderabbit.ai/blog/opus-5-5-model-review) found complementary bug catches: Standard caught 11 issues missed by its production baseline but missed nine baseline catches. Standard beat Max on its 80-pattern OSS set, while harder cases gave mixed benefits to Max. These are pipeline configurations, not individual API effort levels, and the baseline is a production model mix, not Astra alone. This supports trying Opus for a bounded second opinion, not claiming it always reviews better.

[Early Pro-user reports, September 24](https://www.reddit.com/r/ClaudeCode/comments/1woy8o7/is_pro_plan_subscription_usable_with_opuse_55/) are positive about quality and usable sessions. Some still report needing breaks after sustained work. These are self-selected anecdotes immediately after release, without controlled tasks or consumption records; do not turn them into guaranteed hours or quotas.

## Pricing and subscription-aware decisions

| Standard API, USD per million tokens | Opus 5.5 | Astra |
| --- | --- | --- |
| Uncached input | 4 | 10 |
| Output, including reasoning | 20 | 50 |
| Cached input reads | 0.20 | 1 |

Sources: [Opus specification](https://platform.claude.com/docs/en/models/opus-5-5/overview), [Astra specification](https://developers.openai.com/api/docs/models/gpt-6-astra). Astra's full-request rates rise above 272K input tokens. The lower Opus unit price does not guarantee a cheaper completed task because token counts, cache and retries differ.

For existing subscriptions, compare remaining included capacity, expected quality, interruption risk and handoff cost before API prices. Both subscriptions are already paid for; there is no additional per-task cash charge while using included allowance without paid overage. Subscription price ratios are not quota ratios across providers.

Claude Pro has five-hour and weekly limits; Claude surfaces share allowance. Anthropic announced higher five-hour limits with this release, without making Pro unlimited. See [Pro limits](https://support.claude.com/en/articles/8325606-what-is-the-pro-plan), [shared usage](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work) and the release announcement above. Extra usage is separate [paid consumption](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans).

OpenAI's [Codex pricing](https://learn.chatgpt.com/docs/pricing) also describes included, model-dependent usage and possible weekly limits. Use live remaining capacity when available; do not promise unlimited Astra or fixed task counts.

When substantial OpenAI capacity is already included and Claude has a smaller plan, OpenAI is a practical starting point for routine sustained execution. Consider Opus for high-value document synthesis, a bounded difficult diagnosis or a second review, or when OpenAI capacity is constrained. Choose Opus as primary when its expected quality benefit outweighs handoff and interruption costs. Do not reserve it exclusively for emergencies or choose OpenAI solely because its subscription costs more. Start Opus at Medium, increasing effort only for a concrete bottleneck.
