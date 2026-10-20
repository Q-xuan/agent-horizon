---
layout: default
title: Agent Skill
---

# Horizon Agent Skill

The [Horizon skill](https://github.com/Thysrael/Horizon/tree/main/skills/horizon)
helps an AI assistant configure a news radar, generate and tune digests, create
Profiles, schedule delivery, and contribute code. Horizon continues to run the
AI pipeline with the model and credentials in its own configuration.

## Install

Install Horizon following the README, then copy the **entire** `skills/horizon`
directory into your agent's skill directory. The skill and Horizon checkout may
live at different paths. Keep the checkout available for its runtime and docs.

| Agent | Personal skill destination | Reference |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/horizon/` | [Skills](https://code.claude.com/docs/en/skills) |
| Codex | `~/.agents/skills/horizon/` | [Skills](https://developers.openai.com/codex/skills) |
| OpenCode V2 | `~/.config/opencode/skills/horizon/` | [Skills](https://opencode.ai/v2/docs/skills/) |
| OpenClaw | `~/.openclaw/skills/horizon/` | [Skills](https://docs.openclaw.ai/tools/skills) |

For example, from the checkout, when the destination does not already exist:

```bash
mkdir -p ~/.claude/skills
cp -R skills/horizon ~/.claude/skills/horizon
```

Use your agent's project-level installation or extra-directory configuration if
preferred. For example, OpenCode V2 can load the checkout directly by adding its
absolute `skills` directory to the existing configuration's `skills` array.
This avoids maintaining a second copy. Follow the host's refresh/reload behavior
and verify that `horizon` appears in its available skills.

Tell the assistant where the checkout is, or set `HORIZON_PATH`. Python 3.11+
and Horizon's installed dependencies are required to execute the helper. MCP is
optional. A sandboxed agent needs access to the checkout and its runtime.

## Try it

- "Use Horizon to build a Chinese news radar for AI inference and open-source
  tools, with at most ten stories a day."
- "Read today's Horizon digest and give me the original links."
- "Make a Profile for engineering write-ups that emphasizes solutions and
  tradeoffs."
- "Schedule Horizon at 08:00 Asia/Shanghai and send the digest to Feishu."
- "Add an optional content extractor following this repository's conventions."

The helper can also be inspected directly:

```bash
uv run python skills/horizon/scripts/horizon_ops.py run_pipeline --describe
uv run python skills/horizon/scripts/horizon_ops.py validate_config --params '{"check_env": false}'
```

Use `--params-file` for JSON parameters when shell quoting is inconvenient.
`--describe` reads current service parameters without executing the operation.
`ok: true` means the call returned; inspect native results for missing environment
variables and partial failures. See the skill's pipeline reference for details.

## Maintain and evaluate

Maintain one copy under `skills/horizon`. Configuration knowledge belongs in the
existing subject docs, and pipeline behavior belongs in Horizon. The helper
forwards native method parameters and results rather than maintaining another
CLI schema or reimplementing the pipeline. Only its operation allowlist needs
updating when intentionally exposing a new service method.

Run the adapter's offline regression tests after changing it:

```bash
uv sync --extra dev
uv run pytest tests/test_horizon_skill.py -q
```

For behavioral evaluation, use `skills/horizon/evals/scenarios.json` in temporary
checkouts with example configuration and fixture artifacts. Run a scenario with
the skill and in a fresh session without it, using the same model, tools, and
inputs. Record changed files, chosen operations, outputs, and whether each
expected behavior was met. Include the non-trigger examples when checking the
description. Fixture or mocked runs should cover routine evaluation; distinguish
these from live provider and delivery checks.

Adapted design principles: [Agent Skills specification](https://agentskills.io/specification),
[Anthropic skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator),
and [OpenAI skill-creator](https://github.com/openai/skills/tree/main/skills/.system/skill-creator).
