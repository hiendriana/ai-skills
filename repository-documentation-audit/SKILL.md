---
name: repository-documentation-audit
description: Audit and reorganize README.md, AGENTS.md, and docs/ in a software repository. Use when reducing documentation duplication, clarifying documentation ownership, verifying documentation against code, or preparing a repository for a central knowledge base.
---

# Repository documentation audit

Audit and reorganize the current repository's documentation so each topic has
one clear source of truth, useful knowledge is preserved, and documented claims
match the implementation.

## Read first

Before editing, read:

- `guides/documentation-ownership.md`
- `guides/audit-checklist.md`
- `guides/validation.md`

Read `guides/project-metadata.md` only when creating or updating
`docs/project.yaml`.

Use templates only when the repository genuinely needs the corresponding file.
Do not create placeholder documents merely because a template exists.

Repository-specific instructions in the repository's `AGENTS.md` take
precedence over this generic workflow unless they conflict with the user's
explicit request.

## Objectives

Produce a structure where:

- `README.md` onboards human users and developers.
- `AGENTS.md` gives coding agents repository-specific working instructions.
- `docs/` owns durable technical, architectural, domain, deployment,
  operational, recovery, and troubleshooting knowledge.
- Detailed information has one primary owner.
- Other documents summarize and link instead of duplicating details.
- Documentation describes the current implementation.
- The repository can be indexed into a central knowledge base without
  importing contradictory copies.

## Constraints

1. Inspect the repository before editing.
2. Treat existing documentation as potentially outdated.
3. Verify important claims against code, tests, configuration, dependencies,
   CI, and deployment definitions.
4. Do not invent commands, features, architecture, guarantees, dependencies,
   or deployment behavior.
5. Do not silently remove useful knowledge.
6. Do not change application behavior during a documentation audit.
7. Do not perform unrelated refactoring.
8. Do not create empty or speculative documents.
9. Do not expose secrets, tokens, private endpoints, personal identifiers, or
   real credentials.
10. Prefer repository-relative instructions over machine-specific paths.
11. Preserve useful examples and non-obvious caveats.
12. Use relative Markdown links within the repository.
13. Never claim a check passed unless it was actually run.
14. Preserve unrelated user changes already present in the working tree.

## Workflow

### 1. Establish repository state

Determine:

- repository root and project type
- current Git status and existing user changes
- applicable root or nested `AGENTS.md` files
- current documentation structure
- configured build, test, lint, formatting, type-checking, and deployment tools

Do not overwrite unrelated changes.

### 2. Inspect authoritative evidence

Use the checklist in `guides/audit-checklist.md`.

Verify documentation against relevant:

- source entry points and public interfaces
- tests and fixtures
- dependency and task configuration
- example configuration
- container and deployment definitions
- CI workflows
- configuration parsers and schemas
- recent Git history when it clarifies current intent

Current implementation is authoritative. Git history is supporting evidence.

### 3. Build a documentation inventory

Identify:

- exact and near duplication
- contradictions
- obsolete commands, paths, names, or dependencies
- misplaced human, agent, architectural, or operational content
- unsupported claims
- machine-specific or sensitive values
- important behavior present only in code or tests
- broken links and referenced files that no longer exist

### 4. Choose the smallest useful target structure

Apply `guides/documentation-ownership.md`.

Possible files include:

```text
README.md
AGENTS.md
docs/
├── architecture.md
├── domain-rules.md
├── development.md
├── configuration.md
├── deployment.md
├── operations.md
├── troubleshooting.md
├── project.yaml
└── decisions/
```

These are possibilities, not requirements. Prefer one substantial document to
several thin ones.

For infrastructure repositories, prefer the following documentation layout when
supported by verified implementation evidence:

docs/
├── architecture.md
├── services.md
├── networking.md
├── storage.md
├── operations.md
├── security.md
├── troubleshooting.md
├── project.yaml
└── decisions/

Document each deployed service in services.md, including:

- purpose
- dependencies
- exposed ports
- persistent volumes
- networks
- configuration location
- backup considerations
- update procedure
- related documentation

### 5. Reorganize and rewrite

- Assign every detailed topic one primary owner.
- Move rather than copy.
- Replace duplicate detail with a short summary and relative link.
- Keep the README useful without turning it into an internal specification.
- Keep `AGENTS.md` actionable and repository-specific.
- Move durable implementation and operational knowledge into `docs/`.
- Preserve domain invariants, caveats, recovery procedures, and edge cases.
- Remove obsolete historical narrative unless it explains a relevant decision.
- Use ADRs only for durable decisions with meaningful alternatives and
  consequences.
- Replace private values with placeholders.
- Match commands to the repository's actual tools.

When documentation disagrees with implementation:

1. verify the discrepancy
2. document current behavior
3. report the mismatch and uncertainty
4. do not change code merely to make old documentation true

### Collections of independent scripts

When the repository primarily contains independent scripts rather than a single
application:

- Document the repository's overall purpose, organization, and conventions in
  the README.
- Keep implementation details close to the individual script rather than
  expanding the root README.
- Prefer one short description per script with links to script-specific
  documentation when needed.
- Do not create a docs/ directory unless multiple scripts share substantial
  architectural or operational knowledge.
- Treat each script as an independent unit unless shared infrastructure has
  clearly emerged.

### Prefer proportional documentation

When deciding whether to create new documentation:

- Document relationships between components rather than the internal
  implementation of individual components.
- Prefer the smallest documentation structure that adequately supports future
  maintenance.
- As repository complexity grows, documentation may become more detailed.
- Avoid introducing documents whose maintenance cost exceeds their long-term
  value.
- Explain your reasoning whenever you choose not to create additional
  documentation.

### 6. Add a documentation-update policy

Ensure `AGENTS.md` contains a concise repository-specific equivalent of:

> When a change affects installation, usage, architecture, configuration,
> deployment, external dependencies, domain behavior, or operations, update
> the corresponding documentation in the same change.

Ownership rules:

- `README.md`: human-facing onboarding, setup, and usage
- `AGENTS.md`: agent workflow, development rules, and constraints
- `docs/`: durable technical and operational knowledge
- ADRs: durable decisions with meaningful alternatives and consequences

### 7. Validate

Follow `guides/validation.md`.

At minimum:

- inspect the final diff
- verify modified links and referenced paths
- verify documented commands and configuration names
- search for stale terminology and contradictory guidance
- check for introduced secrets or personal values
- run proportionate safe repository checks

Do not run destructive, credential-dependent, migration, restore, production,
or deployment commands merely to validate documentation.

### 8. Report

Report:

1. files changed
2. content moved or removed
3. duplication eliminated
4. documentation added or restructured
5. documentation/code discrepancies
6. checks actually run
7. remaining gaps or uncertainty
8. decisions requiring user input

## Definition of done

The task is complete only when:

- the README can onboard its intended human audience
- `AGENTS.md` enables safe repository-specific agent work
- durable technical knowledge has a clear owner
- obvious duplication and contradiction are removed
- important commands, paths, and claims were checked
- useful knowledge was not silently lost
- modified links work
- no secrets or personal values were introduced
- unrelated user changes were preserved
- executed and unexecuted checks are clearly distinguished
- unresolved ambiguity is explicitly reported

## Invocation examples

Full audit and edit:

```text
$repository-documentation-audit

Audit and reorganize this repository's documentation. Verify all claims against
the current implementation and tests before editing.
```

Audit only:

```text
$repository-documentation-audit

Inspect the documentation and propose a target structure. Do not modify files.
```

Add repository-specific emphasis in the invocation rather than permanently
embedding project facts in this reusable skill.
