# Reusable AI Skills

This repository contains reusable AI Skills for recurring documentation and
knowledge-management work. The checked-out repository is also the live Skill
installation: compatible AI tools discover Skills directly from this directory.

For that reason, each Skill remains directly under the repository root. There
is no intermediate `skills/` directory.

## Repository Philosophy

The goal of this repository is to build a library of durable, reusable AI Skills.

Skills should remain largely platform-neutral. Platform-specific metadata should
be kept small and isolated, while workflows, guides, templates, and supporting
documentation remain portable across AI assistants whenever practical.

## Repository layout

```text
.
├── README.md
├── AGENTS.md
├── .gitignore
├── knowledge-curator/
├── knowledge-janitor/
└── repository-documentation-audit/
```

Each Skill is self-contained and owns its relevant files:

- `SKILL.md` defines the Skill's responsibility, workflow, safety rules, and
  reporting contract.
- `guides/` contains detailed guidance used only by that Skill.
- `templates/` contains templates used only by that Skill.
- `agents/` contains platform-specific metadata belonging to that Skill.

In particular, `agents/openai.yaml` is OpenAI-specific metadata. The main Skill
workflow and supporting guidance should remain platform-neutral as practical.
Add metadata for another platform inside the relevant Skill only after its
actual integration requirements are known; do not invent prospective formats.

## Current Skills

- [`repository-documentation-audit`](repository-documentation-audit/SKILL.md)
  audits and reorganizes repository documentation so topics have clear owners,
  useful knowledge is preserved, and documented claims match implementation.
- [`knowledge-curator`](knowledge-curator/SKILL.md) reviews and
  non-destructively processes Markdown inbox notes into durable domain
  knowledge while preserving source notes, evidence, links, and uncertainty.
- [`knowledge-janitor`](knowledge-janitor/SKILL.md) audits lifecycle state and
  hygiene in personal Markdown knowledge repositories and proposes or applies
  narrowly approved archival and cleanup work.

These descriptions are derived from the current `SKILL.md` entry points.
Platform compatibility should be inferred only from integration or metadata
that is actually present in the relevant Skill.

## Design Principles

Skills in this repository are designed to:

- solve one well-defined problem;
- remain self-contained;
- be non-destructive by default;
- require explicit approval for destructive actions;
- produce clear validation and reporting output;
- minimize platform-specific metadata;
- remain portable across AI platforms whenever practical.

## Install or clone

Clone the repository directly into the live installation path:

```bash
git clone <repository-url> ~/.agents/skills
```

The destination should not already contain files. If a live installation
already exists, inspect and preserve it before replacing it with a clone.

To update an existing checkout without creating a merge commit:

```bash
cd ~/.agents/skills
git status
git pull --ff-only
```

Review or commit local work before pulling. Do not pull over unexplained
changes in the live installation.

## Maintain and publish changes

Inspect the complete working tree and validate the affected Skills before
committing:

```bash
cd ~/.agents/skills
git status
git diff
git diff --check
git add <reviewed-paths>
git commit -m "Describe the focused change"
git push
```

Stage explicit reviewed paths so unrelated live-installation changes are not
included accidentally. Follow the repository-specific maintenance rules in
[`AGENTS.md`](AGENTS.md).

## Sensitive and generated files

Do not commit credentials, tokens, private keys, personal data, `.env` or other
secret files, runtime caches, editor state, build artifacts, or
machine-specific configuration. Before committing, inspect staged changes and
confirm that examples use placeholders rather than real sensitive values.
