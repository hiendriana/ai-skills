# AGENTS.md

## Purpose

This repository is both the Git source and the live installation for reusable
AI Skills. Agents modifying it must preserve the installed top-level layout and
keep changes focused, reviewable, and non-destructive.

## Repository structure

- Top-level directories representing Skills must remain directly under the
  repository root unless the installation mechanism is deliberately changed.
- Do not introduce a nested `skills/` directory without first confirming that
  every consuming tool supports it.
- Repository-wide documentation belongs in `README.md`, `AGENTS.md`, or a
  genuinely shared document.
- Skill-specific material belongs inside the corresponding Skill directory.

## Skill ownership

Each Skill must remain self-contained. Typical ownership is:

- `SKILL.md`: entry point, responsibility, workflow, safety rules, modes, and
  reporting contract.
- `guides/`: detailed Skill-specific guidance.
- `templates/`: templates used only by that Skill.
- `agents/`: platform-specific metadata belonging to that Skill.

Do not move `agents/openai.yaml` to a central adapter directory. Add another
platform-specific file or adapter only after confirming that platform's actual
requirements. Do not invent prospective formats such as `claude.yaml`.

## Modifying Skills

- Preserve existing behavior unless a behavioral change is explicitly
  requested.
- Keep each Skill narrowly focused.
- Prefer updating existing guidance over creating overlapping documents.
- Do not modify unrelated Skills during a focused change.
- Preserve non-destructive defaults and explicit-approval boundaries.
- Keep reporting and validation instructions consistent with actual behavior.
- Avoid references to files that do not exist in the installed Skill.
- When a change affects installation, usage, behavior, safety, dependencies,
  structure, or maintenance, update the owning documentation in the same
  change.

## Shared content

Do not create shared documentation merely because multiple Skills use similar
wording. Create or move content into `shared/` only when:

- at least two Skills genuinely depend on the same maintained guidance;
- central ownership reduces real duplication;
- the Skills can reference it without becoming harder to install or
  understand; and
- the shared file remains available in the live installation layout.

Prefer self-contained Skills over excessive indirection. It is acceptable for
`shared/` not to exist or to remain empty.

## Templates

A repository-level `templates/` directory may contain only templates reused by
multiple Skills. Skill-specific templates remain inside the Skill. Do not
create placeholder templates.

## Validation

After changing a Skill:

1. Inspect the complete Skill diff.
2. Validate relative Markdown links and referenced guide paths.
3. Verify that `agents/openai.yaml` is syntactically plausible and still
   describes the actual Skill.
4. Check that safety rules, approval boundaries, reporting, and documented
   behavior remain consistent.
5. Search changed and candidate tracked files for accidental secrets, personal
   data, and machine-specific configuration.
6. Run `git diff --check`.
7. Report files inspected, files changed, validation performed, and remaining
   uncertainty.

Do not claim a validation passed unless it was actually run. Do not commit or
push unless the user explicitly requests it.
