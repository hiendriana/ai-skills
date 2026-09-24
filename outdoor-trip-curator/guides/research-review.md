# Independent Evidence Review

Use this protocol after research and assessment and before writing
interpretation-sensitive external findings into canonical trip knowledge. It is
an evidence gate; it does not replace repository/output validation after writing.

## Select findings for review

Apply the full review to findings whose meaning depends on interpretation,
synthesis, classification, conversion, or route matching. Give particular
scrutiny to:

- difficulty and grades;
- route identity and variants;
- activity classification, including ski or splitboard suitability;
- glacier involvement and objective hazards;
- protection and equipment requirements;
- approach and descent;
- access restrictions and seasonality; and
- any safety-relevant conclusion.

Simple metadata explicitly stated by an authoritative source, such as an
unambiguous place name or contact detail, may receive a proportionate source
check instead. When in doubt, use the full review.

## Prepare the review packet

Freeze candidate findings before review and give the reviewer only:

1. each candidate claim, with its intended canonical field or wording;
2. the original supporting evidence or direct source locations, including enough
   context to evaluate qualifications and route identity;
3. the applicable destination-repository policy, schema, and controlled-value
   rules; and
4. this review protocol.

Do not include the researcher's chain of thought, arguments defending the claim,
or preferred outcome. Supply additional research context only when it is needed
to investigate a specific review finding. The packet must preserve source dates,
attribution, grading systems, and distinctions among quoted facts, attributed
opinions, and inference.

## Preserve independence

When the runtime supports fresh agents, subagents, or isolated contexts, use a
fresh reviewer context that did not perform the research. The workflow remains
provider-agnostic: use the runtime's available isolation mechanism rather than a
provider-specific command or configuration.

If isolation is unavailable, perform a separate adversarial verification pass:
set aside the researcher's conclusions, re-open the supplied evidence, and test
each candidate from scratch. Report that this was a distinct adversarial pass,
not a context-independent review. Never claim reviewer independence that the
runtime did not provide.

## Review adversarially

Try to falsify each consequential candidate rather than looking only for
confirmation. Determine:

- whether the cited evidence establishes the exact claim;
- whether the claim is explicit or inferred;
- whether synthesis introduced a classification or grading-system conversion;
- whether the source describes the exact route and variant rather than a nearby,
  similarly named, shortened, extended, summer, winter, ski, or climbing route;
- whether subjective or experiential language became an objective fact;
- whether credible sources conflict;
- whether qualifications, scope, dates, or uncertainty were lost; and
- whether a safety-relevant conclusion is stronger than the evidence.

Consult the supplied original sources rather than relying on the candidate's
citation label or summary. A generally relevant source is not evidence for a
specific statement it does not make. Distinguish absence of evidence from
evidence that a feature is absent.

### Difficulty and grading

A grade attributed to a source must be stated by that source for the exact route
or variant. Preserve the source's grading system when possible. Do not derive or
convert an overall grade from slope angles, pitches, hazards, narrative route
characteristics, or a grade in another system unless the destination repository
explicitly defines and permits that conversion.

For example, descriptions that appear compatible with an alpine grade such as
`ZS+` do not establish that grade. Reject or revise an unsupported derived grade;
if repository policy permits recorded inference, label it explicitly as inference
with its basis and uncertainty rather than presenting it as sourced fact.

## Return a review result

Return one overall outcome and itemized findings:

- `PASS` — the evidence supports the candidate at the proposed specificity and
  confidence.
- `REVISE` — the candidate misinterprets, overstates, transforms, or incompletely
  represents available evidence and can reasonably be corrected. Identify the
  defect and the evidence that must be represented, but do not silently rewrite
  canonical knowledge in the review step.
- `ESCALATE` — the evidence is ambiguous or conflicting, human judgment is
  required, or the claim cannot be established reliably. State the unresolved
  question and safe disposition.

The curator owns the response. On `PASS`, it may write the reviewed candidate. On
`REVISE`, it may make one correction to the candidate and submit that revision
for another review. If the second review does not pass, use `ESCALATE` or preserve
the uncertainty under repository policy; do not retry again. On `ESCALATE`, do
not write the disputed proposition as fact. Record uncertainty only where the
repository permits it, or defer the canonical change for human judgment.

Keep the review result with the working report when practical, but do not invent
a persistent review database or add review metadata to canonical notes unless
the destination repository requires it.
