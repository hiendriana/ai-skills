# Documentation ownership

## README.md

Audience: humans discovering, installing, running, or contributing to the
project.

Usually owns:

- purpose and status
- primary capabilities
- prerequisites
- installation and setup
- common configuration and usage
- basic development commands
- brief architecture or deployment summaries
- links to detailed documentation

Should not own:

- detailed agent instructions
- exhaustive internals
- long architecture explanations
- full operations or recovery runbooks
- duplicated validation policy
- obsolete project history
- private values

## AGENTS.md

Audience: Codex and other coding agents modifying the repository.

Usually owns:

- concise repository purpose
- important source and test layout
- architectural boundaries
- domain invariants
- repository-specific conventions
- package and dependency rules
- validation commands
- task-completion expectations
- sensitive or generated files
- secret-handling rules
- common traps
- documentation update requirements

Should not own:

- full end-user installation tutorials
- complete usage guides
- long deployment procedures
- full architecture documents
- generic advice with no repository-specific value

## docs/

Audience: humans and agents needing durable detail.

Possible ownership:

- `architecture.md`: components, boundaries, dependency direction, data flow
- `domain-rules.md`: invariants, precedence, edge cases, state transitions
- `development.md`: detailed development and debugging workflows
- `configuration.md`: configuration model, defaults, precedence, variables
- `deployment.md`: deployment architecture, environments, rollback
- `operations.md`: maintenance, health checks, backups, upgrades
- `troubleshooting.md`: symptoms, diagnoses, safe resolutions
- `decisions/`: durable architectural decision records
- `project.yaml`: stable metadata for cross-repository indexing

Create only documents supported by meaningful verified content.

## Ownership test

For each section, ask:

1. Who needs it?
2. At what point in their workflow?
3. How frequently does it change?
4. What evidence verifies it?
5. Which one file should own the detailed version?
6. Where should only a summary and link remain?

## Collections of independent scripts

Repositories containing multiple unrelated scripts should optimize for
discoverability rather than detailed centralized documentation.

The root README should typically contain:

- repository purpose
- organization
- list of scripts
- one short description of each script
- common development conventions
- guidance for adding new scripts

Avoid moving detailed implementation behavior from the scripts into the root
README. Script-specific behavior should remain with the script or in
script-specific documentation if it becomes substantial.