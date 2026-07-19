# Audit checklist

Use judgment; not every item applies.

## Repository state

- Locate the repository root.
- Inspect `git status`.
- Preserve uncommitted user changes.
- Find applicable root and nested `AGENTS.md` files.
- Identify monorepo boundaries and project type.

## Existing documentation

Inspect when present:

- `README.md`
- `AGENTS.md`
- `CONTRIBUTING.md`
- `CHANGELOG.md`
- `SECURITY.md`
- `docs/`
- ADRs and runbooks
- examples and sample configuration
- diagrams

## Implementation evidence

Inspect relevant:

- entry points and CLI definitions
- public APIs
- source and test layout
- domain models and boundaries
- tests and fixtures
- dependency manifests and lockfiles
- task runners and build configuration
- formatter, linter, and type-check configuration
- Dockerfiles and Compose files
- infrastructure-as-code
- CI/CD workflows
- migrations
- configuration parsing
- environment variable access
- health checks
- backup and restore scripts
- `.gitignore`
- release configuration

## Common defects

Look for:

- exact or paraphrased duplication
- contradictory commands or policies
- stale package, module, service, or path names
- obsolete deployment mechanisms
- features described but absent
- implemented behavior left undocumented
- plans presented as current behavior
- absolute machine-specific paths
- wrong shell or platform instructions
- nonexistent environment variables
- missing prerequisites or safety warnings
- secrets or real personal values
- architecture claims unsupported by code
- broken files, links, or anchors
- human guidance misplaced in `AGENTS.md`
- agent guidance misplaced in the README

## Duplication decisions

Keep short summaries when useful. Replace duplicated detail with links when it:

- changes frequently
- defines invariants
- specifies configuration
- describes operations or recovery
- defines architecture
- is expensive to keep synchronized
