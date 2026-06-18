---
description: Weekly review of my Claude Code activity — usage summary + skills worth codifying (analysis only, no changes)
allowed-tools: Bash, Read, Glob, Grep
---

You are producing my **weekly Claude Code review** for the mariadb-docs project. This is
**analysis only — do not edit files, commit, or change any Jira/Slack state.** Produce a concise
report at the end.

## Inputs (all LOCAL — that's why this runs locally, not as a cloud routine)

1. **Session transcripts** — under `~/.claude/projects/-Users-tauseefkhanmdb-Documents-GitHub-mariadb-docs/`.
   Find session files modified in the last 7 days:
   `find ~/.claude/projects/-Users-tauseefkhanmdb-Documents-GitHub-mariadb-docs -name '*.jsonl' -mtime -7 -print` (also check `.json`).
   Sample / skim them (they can be large — use `jq`/`grep` to pull user messages, tool names, and
   DOCS-XXXX mentions rather than reading whole files).
2. **Research paper trail** — `research/*.md` in the repo (gitignored). List those modified in the
   last 7 days and read them for what was worked on and verified.
3. **DOCS tickets** — derive the set of `DOCS-XXXX` ids touched this week from the transcripts and
   research notes. If the Atlassian (`atlassian-mariadb` / Rovo) MCP is available, optionally fetch
   their current status; if not, just list the ids.

## Steps

1. Establish the window: `date -u` → the last 7 days.
2. Gather the three inputs above. Note explicitly anything you could NOT access (e.g. no transcripts
   found, MCP unavailable) — never imply coverage you didn't have.
3. Identify **recurring patterns** across the week: repeated multi-step sequences, the same kind of
   verification done over and over, repeated manual fixes, repeated search shapes, etc.

## Output (concise report)

### 1. Usage summary
- Sessions this week (count + rough active days).
- DOCS tickets worked, with one-line outcome each.
- Notable one-offs (investigations, Slack drafts, config changes).
- What I could not measure (be honest — e.g. no token/billing telemetry is available locally).

### 2. Worth codifying into a skill / command?
For each recurring pattern that showed up **3+ times** or cost real repeated effort:
- **Pattern** — what I keep doing.
- **Evidence** — which sessions/tickets it appeared in.
- **Proposal** — a concrete new skill or `/slash-command` (name + one-line purpose), or "fold into
  an existing skill X".
- **Confidence** — high/medium/low.

End with a single recommended next action (e.g. "file a propose-improvement for /foo"), but do NOT
act on it — leave that to me.
