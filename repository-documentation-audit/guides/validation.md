# Validation guide

## Commands

For every documented command, verify:

- the executable or task exists
- the package manager matches repository configuration
- flags are supported
- required working directory and environment are clear
- the command is safe for its stated purpose
- expected results are not overstated

Prefer safe checks such as:

- `--help`
- `--version`
- dry-run modes
- listing configured tasks
- local tests
- linting
- formatting checks
- type checks

Do not run solely for documentation validation:

- production deployments
- destructive cleanup
- irreversible migrations
- restore operations
- remote mutations
- commands requiring real credentials

## Links and paths

Verify:

- relative links resolve from their containing file
- anchors match headings
- filename casing is correct
- inbound links are updated after renames
- referenced files and directories exist
- links do not expose private local paths

## Consistency

Search for:

- old project or service names
- stale commands
- duplicate policies
- conflicting architecture claims
- obsolete configuration variables
- references to removed files

## Safety

Check the final changes for:

- tokens, passwords, and API keys
- private hostnames or endpoints
- personal identifiers
- real configuration values that should be placeholders
- unrelated application-code modifications

## Final diff

Confirm:

- useful caveats were preserved
- moved content reached the intended owner
- summaries accurately describe linked detail
- no unrelated user change was overwritten
- no empty placeholder document was added
- formatting is consistent
- the report lists only checks actually run
