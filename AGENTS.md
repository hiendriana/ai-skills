# AGENTS.md

## Purpose

This repository contains the source for reusable AI Skills.

Each Skill is a self-contained unit with its own documentation, guides, templates, and platform-specific metadata.

---

## Repository Ownership

Repository-wide documentation belongs in:

- README.md
- shared/

Skill-specific documentation belongs inside the corresponding Skill directory.

Do not move Skill-specific guidance into shared documentation unless it is duplicated across multiple Skills.

---

## Modifying Skills

When changing a Skill:

- Preserve its public behavior unless explicitly requested.
- Keep the Skill self-contained.
- Prefer extending an existing guide over creating additional files.
- Avoid duplicating guidance already present in another guide.

---

## Shared Documentation

Only create or modify files under `shared/` when the same guidance is genuinely applicable to multiple Skills.

Avoid premature abstraction.

---

## Platform-Specific Metadata

Platform-specific configuration belongs only in the Skill's `agents/` directory.

Examples:

- `agents/openai.yaml`
- future `agents/claude.yaml`

Do not move platform-specific metadata into repository-wide documentation.

---

## Skill Design Principles

Every Skill should:

- have a single responsibility;
- be non-destructive by default;
- support review before apply whenever practical;
- clearly separate reusable guidance from platform metadata;
- produce a validation report after significant changes.

---

## Validation

After modifying a Skill:

- validate its internal links;
- validate referenced guides;
- ensure documentation matches behavior;
- ensure reporting and safety guarantees remain consistent.

Do not modify unrelated Skills during the same change unless explicitly requested.