# AGENTS.md

## Purpose

This repository is both the Git source and the live installation for reusable
AI Skills whose maintenance lifecycle genuinely spans repositories. Agents
modifying it must preserve the installed top-level layout and keep changes
focused, reviewable, and non-destructive.

## Repository structure

- Top-level directories representing Skills must remain directly under the
  repository root unless the installation mechanism is deliberately changed.
- Do not introduce a nested `skills/` directory without first confirming that
  every consuming tool supports it.
- Repository-wide documentation belongs in `README.md`, `AGENTS.md`, or a
  genuinely shared document.
- Skill-specific material belongs inside the corresponding Skill directory.

## Skill ownership

Keep a Skill here only when its change lifecycle is genuinely cross-repository.
A Skill does not belong here merely because it is portable: repository-coupled
Skills may live with their owning repository while remaining reusable in design.
`repository-documentation-audit` remains here because it is independently
applicable across repositories.

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
- Preserve non-destructive defaults and explicit-approval boundaries, except
  where an applicable repository policy explicitly authorizes a scheduled
  branch-and-PR preparation workflow. Such a workflow never authorizes merge.
- Keep reporting and validation instructions consistent with actual behavior.
- Avoid references to files that do not exist in the installed Skill.
- When a change affects installation, usage, behavior, safety, dependencies,
  structure, or maintenance, update the owning documentation in the same
  change.

## Templates

Keep Skill-specific templates inside the owning Skill. Do not create placeholder
or repository-level shared templates without a demonstrated cross-Skill need.

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
