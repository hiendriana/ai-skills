# Project metadata guidance

Use `docs/project.yaml` only when structured metadata supports cross-repository
indexing, automation, or a central knowledge base.

## Principles

- Include stable, verifiable facts only.
- Keep the schema small.
- Omit irrelevant or uncertain fields.
- Never include secrets, private URLs, usernames, personal identifiers, or
  machine-specific paths.
- Use prose documentation for nuance and rationale.
- Update metadata when its facts change.

## Suggested fields

```yaml
name: example-project
status: active
purpose: One-sentence verified purpose
project_type: service
runtime:
  language: python
  version: "3.12"
architecture:
  style: hexagonal
deployment:
  type: docker-compose
dependencies:
  - postgres
external_services: []
notifications: []
related_projects: []
documentation:
  architecture: architecture.md
```

Only `name`, `status`, and `purpose` are normally expected when the file exists.
All other fields are optional.

Suggested `status` values:

- `active`
- `maintenance`
- `experimental`
- `archived`

Suggested `project_type` values:

- `cli`
- `library`
- `service`
- `web-application`
- `static-site`
- `infrastructure`
- `template`
- `monorepo`

Verify every value against repository evidence.
