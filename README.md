# Reusable AI Skills

This repository contains reusable AI Skills whose maintenance lifecycle genuinely
spans repositories. The checked-out repository is also the live Skill
installation: compatible AI tools discover Skills directly from this directory.

For that reason, each Skill remains directly under the repository root. There is no intermediate `skills/` directory.

## Repository Philosophy

Design Skills for reuse, organize repositories around change boundaries, and
keep AI-provider integration at the edges. Portability alone does not determine
ownership: a reusable Skill whose behavior changes with one repository may live
with that repository. Skills retained here should have a genuinely
cross-repository lifecycle.

Skill behavior should remain provider-neutral where practical. Provider-specific
metadata should be small and isolated rather than defining the architecture.
Destination repositories continue to own their paths, schemas, lifecycle rules,
and personal tooling conventions.

## Repository layout

```text
.
├── README.md
├── AGENTS.md
├── .gitignore
└── repository-documentation-audit/
```

Each Skill is self-contained:

- `SKILL.md` defines responsibility, workflow, safety rules, and reporting contract.
- `guides/` contains detailed reusable guidance used only by that Skill.
- `templates/` contains reusable templates used only by that Skill.
- `agents/` contains platform-specific metadata belonging to that Skill.

In particular, `agents/openai.yaml` is OpenAI-specific metadata. Add metadata for another platform only after its actual integration requirements are known.

## Current Skills

- [`repository-documentation-audit`](repository-documentation-audit/SKILL.md) audits and reorganizes repository documentation so topics have clear owners, useful knowledge is preserved, and documented claims match implementation.

Knowledge-base operational Skills are canonically maintained in the
[`knowledge-base` repository](https://github.com/hiendriana/knowledge-base/tree/main/skills)
because their change lifecycle is coupled to that repository. They remain
reusable in design; this repository no longer distributes them.

Platform compatibility should be inferred only from integration or metadata actually present in the relevant Skill.

## Design Principles

Skills should:

- solve one well-defined problem;
- remain self-contained;
- defer repository-specific policy and data models to the target repository;
- be non-destructive by default;
- require explicit approval for destructive actions, except narrowly scoped
  scheduled branch-and-PR preparation explicitly authorized by the target
  repository policy, with human review before merge;
- produce clear validation and reporting output;
- minimize platform-specific metadata;
- remain portable across AI platforms whenever practical.

## Install or clone

To consume `repository-documentation-audit` from this repository as a live
top-level Skill, clone the repository directly into the live installation path:

```bash
git clone <repository-url> ~/.agents/skills
```

The destination should not already contain files. If a live installation already exists, inspect and preserve it before replacing it with a clone.

To update an existing checkout without creating a merge commit:

```bash
cd ~/.agents/skills
git status
git pull --ff-only
```

Review or commit local work before pulling. Do not pull over unexplained changes in the live installation.

## Maintain and publish changes

Inspect the complete working tree and validate affected Skills before committing:

```bash
cd ~/.agents/skills
git status
git diff
git diff --check
git add <reviewed-paths>
git commit -m "Describe the focused change"
git push
```

Stage explicit reviewed paths so unrelated live-installation changes are not included accidentally. Follow [`AGENTS.md`](AGENTS.md).

## Sensitive and generated files

Do not commit credentials, tokens, private keys, personal data, `.env` or other secret files, runtime caches, editor state, build artifacts, or machine-specific configuration. Before committing, inspect staged changes and confirm examples use placeholders rather than real sensitive values.
