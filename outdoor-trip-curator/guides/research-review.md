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

## Distinguish epistemic status from review outcome

Classify the support for each candidate while reviewing it:

- `SOURCED` — the source explicitly establishes the claim.
- `INFERRED` — the claim is a conclusion derived from identifiable sourced
  evidence rather than something the source explicitly states.
- `UNRESOLVED` — the available evidence does not support a sufficiently reliable
  fact or useful inference.

These are review concepts, not additional workflow outcomes or required
persistent metadata. Do not impose them as fields on a destination repository.
The review outcome remains `PASS`, `REVISE`, or `ESCALATE`; a well-supported and
clearly represented `INFERRED` candidate can receive `PASS`.

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
confirmation. Evaluate source fidelity and inference quality independently.

### Source fidelity

Determine:

- whether the cited evidence establishes the exact claim;
- whether the claim is explicit or inferred;
- whether the source describes the exact route and variant rather than a nearby,
  similarly named, shortened, extended, summer, winter, ski, or climbing route;
- whether source terminology, grades, and qualifications are represented
  accurately;
- whether subjective or experiential language became an objective fact;
- whether credible sources conflict;
- whether qualifications, scope, dates, or uncertainty were lost; and
- whether a safety-relevant conclusion is stronger than the evidence.

Consult the supplied original sources rather than relying on the candidate's
citation label or summary. A generally relevant source is not evidence for a
specific statement it does not make. Distinguish absence of evidence from
evidence that a feature is absent.

### Inference quality

For a candidate that extends beyond an explicit source statement, determine:

- whether the conclusion follows reasonably from the cited evidence;
- whether synthesis introduced a classification or grading-system conversion;
- whether material assumptions and the evidentiary basis remain visible;
- whether plausible alternative interpretations materially weaken the result;
- whether confidence and uncertainty match the strength of the evidence;
- whether the conclusion is useful enough to retain; and
- whether its wording and intended location clearly distinguish it from a
  source-attributed fact.

Attempt to falsify important inferences, including by considering credible
alternatives, rather than accepting a plausible narrative at face value. Hidden,
misattributed, weak, or overconfident inference requires `REVISE` or `ESCALATE`;
the fact that a conclusion is inferred does not by itself prevent `PASS`.

### Difficulty and grading

A grade attributed to a source must be stated by that source for the exact route
or variant. Preserve the source's grading system when possible. A derived grade
or cross-system interpretation may be retained when it is useful, its supporting
evidence is identifiable, the derivation is reasonable, uncertainty is visible,
and destination-repository policy permits that representation. Label it as an
inference; never attribute it to a source that does not state it.

For example, reported UIAA II climbing, exposure, unmarked terrain, and demanding
route-finding do not establish that a source assigns an SAC alpine grade. A
candidate such as "Inferred overall character: approximately ZS based on the
reported UIAA II climbing, exposure, unmarked terrain, and route-finding demands.
No checked source assigns an SAC alpine grade" may pass if the reviewer finds the
derivation defensible. "Tourentipp grades the route ZS+" must be revised unless
Tourentipp explicitly provides that grade for the exact route or variant.

Respect the destination repository's distinction between structured and prose
content. If a structured grade field is defined as authoritative or source-backed,
keep a permitted inferred grade in explanatory prose rather than placing it in
that field. This protocol does not define a universal storage schema.

## Return a review result

Return one overall outcome and itemized findings:

- `PASS` — the candidate is either explicitly supported or a reasonable,
  clearly identified inference, at the proposed specificity and confidence.
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
