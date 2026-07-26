# Bundle Review

Treat a directory containing `capture.md` with `capture_format: bundle-v1` as
one indivisible capture. Support manifests declaring PDF, JPEG, PNG, and WebP
source files. Do not extract new knowledge or rerun OCR during lifecycle review;
route content curation back to `knowledge-curator`.

## Structural gate

Require repository policy to allow binary capture bundles and define their
active inbox, processed recycle bin, file-size or version-control constraints,
retention, and recoverable removal workflow. Audit only when policy is absent or
ambiguous.

Verify that:

- `capture.md` is the only manifest and uses `capture_format: bundle-v1`;
- every other regular file is declared exactly once in `source_files`;
- every declared relative path stays within the bundle and exists;
- no nested directory, symlink, traversal, undeclared file, or duplicate path
  exists;
- detected type, byte size, and SHA-256 match the manifest; and
- status, extraction coverage, limitations, and destinations are unambiguous.

Use a safe YAML loader and reject aliases, custom tags, duplicate keys, invalid
field types, an empty `source_files` sequence, `capture.md` as a source, absolute
or non-scalar source paths, path normalization, and duplicates after applying
repository and filesystem case behavior. Require each source path to be one
filename without slash, empty component, `.` or `..`. Require every source entry
to contain valid type, size, hash, and its own extraction record; do not accept
one global extraction record for multiple sources.

Any structural or hash failure makes the whole bundle ineligible. Never repair
or remove one member as incidental cleanup.

## Link and Git gate

Search inbound links to the bundle directory, manifest, and every source file.
Verify tracking and committed-history evidence separately for every member at
its exact processed path. A commit containing only the manifest, only an
attachment, or an earlier active-inbox path is insufficient.

Review every `integrated_into` destination without extracting new knowledge.
Unresolved OCR or visual limitations block removal when they leave integration
completeness uncertain. Empty OCR alone is not a blocker when the processed
record establishes that the image contained no meaningful text.

## Review and removal

In deletion review, report the exact bundle directory and enumerate every
member path with its hash, link, Git, destination, and retention result. Explain
that removal discards the convenient working-tree copy of the original source
and its provenance manifest.

Require later approval naming every exact member path. Approval of a directory,
one member, or a broad cleanup is insufficient. Immediately before removal,
repeat every gate and use only the repository's documented recoverable Git
workflow with the approved exact file list. Never use a recursive directory
deletion or a broad pathspec. After all approved members are removed, verify the
exact reviewed bundle directory is empty and remove that directory with a
nonrecursive empty-directory operation. This removes no capture data and needs
no separate approval; stop if any entry remains.
