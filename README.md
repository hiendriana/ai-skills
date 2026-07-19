# AI Skills

Reusable AI Skills for Codex, Claude Code, and future AI coding assistants.

This repository is the source of truth for reusable, vendor-neutral Skills that automate recurring engineering and knowledge-management workflows.

Each Skill encapsulates a single responsibility and can be installed into compatible AI tooling. Whenever possible, Skills are designed so that only a small adapter is platform-specific while the workflow, guides, templates, and documentation remain portable.

---

# Repository Structure

```text
.
├── README.md
├── AGENTS.md
├── shared/
│   ├── documentation-principles.md
│   ├── prompt-writing-guidelines.md
│   ├── validation-checklist.md
│   └── ...
├── skills/
│   ├── repository-documentation-audit/
│   ├── knowledge-curator/
│   ├── knowledge-janitor/
│   └── ...
└── templates/
    └── ...
```

## `skills/`

Contains one directory per reusable Skill.

Each Skill is self-contained and typically includes:

```text
skill-name/
├── SKILL.md
├── guides/
├── templates/        (optional)
└── agents/
    ├── openai.yaml
    └── ...
```

### `SKILL.md`

The entry point describing the Skill's purpose, workflow, responsibilities, safety guarantees, and reporting contract.

### `guides/`

Detailed guidance referenced by the Skill.

### `templates/`

Reusable templates used by the Skill when appropriate.

### `agents/`

Platform-specific metadata required by AI tooling.

For example:

- `openai.yaml`
- `claude.yaml` (future)
- other tool-specific metadata

The Skill itself should remain as platform-independent as possible.

---

## `shared/`

Documentation shared across multiple Skills.

Examples include:

- documentation principles
- validation checklists
- prompt-writing guidelines
- naming conventions

Only place information here once genuine duplication exists.

---

## `templates/`

Repository-wide templates that are useful across multiple Skills.

Avoid creating templates that are only used by a single Skill.

---

# Design Principles

Every Skill should:

- have a single responsibility
- be reusable
- be largely platform independent
- be non-destructive by default
- require explicit approval before destructive actions
- support review before apply whenever practical
- produce clear reports
- avoid duplicated guidance
- prefer updating existing information over creating duplicates

---

# Current Skills

## Repository Documentation Audit

Audits repository documentation and improves its structure while preserving the repository as the source of truth.

## Knowledge Curator

Processes captured knowledge from the inbox and integrates durable information into the knowledge base.

## Knowledge Janitor

Reviews the knowledge base for lifecycle, hygiene, duplication, stale information, and archive eligibility.

---

# Installation

Clone this repository into your local AI Skills directory.

Example:

```bash
git clone <repository-url> ~/.agents/skills
```

Compatible AI tools can then discover or install Skills from this location according to their own conventions.

---

# Versioning

Each Skill evolves independently.

Changes should be:

- focused
- reviewable
- backward compatible whenever practical

Prefer small commits over large refactorings.

---

# Contributing

When creating or modifying a Skill:

1. Keep responsibilities narrowly focused.
2. Avoid duplicating shared guidance.
3. Preserve backward compatibility where practical.
4. Validate the Skill before committing.
5. Update documentation when behavior changes.

---

# Long-Term Vision

The goal of this repository is to build a library of reusable AI Skills that can be shared across projects and AI platforms.

Whenever possible, workflows, guides, templates, and documentation should remain vendor-neutral, while only minimal metadata inside each Skill's `agents/` directory is platform-specific.