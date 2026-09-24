# Reusable AI Skills

This repository contains reusable AI Skills for recurring documentation and knowledge-management work. The checked-out repository is also the live Skill installation: compatible AI tools discover Skills directly from this directory.

For that reason, each Skill remains directly under the repository root. There is no intermediate `skills/` directory.

## Repository Philosophy

The goal is a library of durable, reusable AI Skills. Skills should remain largely platform-neutral. Platform-specific metadata should be small and isolated, while workflows and supporting guidance remain portable where practical. Repository-specific paths, schemas, lifecycle rules, and personal tooling conventions belong in the repository that owns them rather than in reusable Skills.

## Repository layout

```text
.
├── README.md
├── AGENTS.md
├── .gitignore
├── book-curator/
├── knowledge-curator/
├── knowledge-janitor/
├── outdoor-trip-curator/
├── snowboard-curator/
└── repository-documentation-audit/
```

Each Skill is self-contained:

- `SKILL.md` defines responsibility, workflow, safety rules, and reporting contract.
- `guides/` contains detailed reusable guidance used only by that Skill.
- `templates/` contains reusable templates used only by that Skill.
- `agents/` contains platform-specific metadata belonging to that Skill.

In particular, `agents/openai.yaml` is OpenAI-specific metadata. Add metadata for another platform only after its actual integration requirements are known.

## Current Skills

- [`book-curator`](book-curator/SKILL.md) identifies, deduplicates, imports, researches, and safely enriches book records while deferring schema, field ownership, controlled values, paths, templates, and views to the destination knowledge base.
- [`repository-documentation-audit`](repository-documentation-audit/SKILL.md) audits and reorganizes repository documentation so topics have clear owners, useful knowledge is preserved, and documented claims match implementation.
- [`knowledge-curator`](knowledge-curator/SKILL.md) reviews and non-destructively processes Markdown notes and manifested PDF or image inbox bundles into durable domain knowledge while preserving originals, evidence, links, and uncertainty. Local PDF extraction and English/German OCR require Tesseract and Poppler tools.
- [`knowledge-janitor`](knowledge-janitor/SKILL.md) audits lifecycle state and hygiene for Markdown captures and manifested PDF or image bundles and proposes or applies narrowly approved archival and cleanup work.
- [`outdoor-trip-curator`](outdoor-trip-curator/SKILL.md) researches and organizes outdoor trips and route ideas, independently reviews interpretation-sensitive evidence before canonical writing, and defers repository-specific schemas, paths, lifecycle, indexes, and tooling conventions to the target repository.
- [`snowboard-curator`](snowboard-curator/SKILL.md) researches exact snowboard models and seasons, creates or updates sourced reports, and adds personal sizing and a test plan when requested. Repository-specific locations and rider context stay with the destination repository.

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

Clone the repository directly into the live installation path:

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
