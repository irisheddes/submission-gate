# Cartulary — Executive Summary

*BSC AI Factory Incubation Programme, Call 3. Submitted 2026-09-08.*
*Length as submitted: **5 pages** (PDF, A4). FICTIONAL — see README.md.*

---

## Page 1 · The problem

Agentic AI has a working architecture for knowledge work, and European public bodies cannot
legally use it.

The architecture is interpretable context methodology: instead of hiding a process inside
model weights or framework code, you express it as a folder of plain files a person can read
— what the agent is, what rules it follows, what it may and may not load at each step. One
model walks the structure. A civil servant can open any folder and see exactly what the system
was told. For public administration this is not a nicety; an automated decision a citizen can
appeal has to be inspectable, and a folder is inspectable in a way an embedding is not.

The platforms that host these workspaces are American. That places the workspace — which for
a municipality contains case files, correspondence and the reasoning applied to them — on
infrastructure subject to third-country access, under a transfer regime European public
bodies have spent three years trying to reconcile with Chapter V of the GDPR. Add the AI
Act's obligations for public-sector deployments and the outcome is predictable: pilots that
never leave the sandbox, procurement processes that stall at the data-protection review, and
a working methodology adopted everywhere except the sector that needs its interpretability
most.

The methodology is not the gap. The hosting is.

## Page 2 · What we build

Cartulary is sovereign hosting for interpretable context workspaces: the same folder-shaped
architecture, run entirely on European infrastructure, with the guarantees a public body has
to be able to write into a contract.

Three things, none of which is a model:

1. **Residency with proof.** Every workspace, every document and every inference stays in the
   EU. Not a policy statement — a per-request log a data-protection officer can audit, naming
   which node served it.
2. **The folder is the record.** Because the workspace is plain files, the archive of what the
   agent was told is the workspace itself, versioned. When a decision is challenged two years
   later, the exact context that produced it can be reconstructed and read.
3. **Inference on EU compute.** Open-weight models served from European hardware, so the
   sovereignty guarantee survives the part where the work actually happens.

### Why this is infrastructure and not policy

A residency promise written into a service agreement is a request. A residency guarantee
enforced by the fact that no node outside the Union can serve the request is a constraint.
Public procurement has learned to tell the difference, which is why so many pilots die at the
data-protection review: the vendor offers the first and the reviewer needs the second.

The same distinction shapes the product. An interpretable workspace already separates the
part the operator owns — their cases, their documents, their decisions — from the part the
platform maintains. Hosting that split is the whole job: the operator's half never leaves the
jurisdiction, the platform's half updates underneath it, and neither can silently absorb the
other. We hold the split as a hard boundary rather than a convention, because a convention is
something an upgrade can quietly cross.

And because the workspace is files under version control, it accretes. The record of what the
system was told is not a log written beside the work — it *is* the work, at every past
version. A decision challenged in 2029 is reconstructed by checking out the workspace as it
stood, not by trusting a description of it.

The methodology is published and open (Van Clief & McDermott, *Folder Structure as Agentic
Architecture*, arXiv:2603.16021, MIT-licensed). We did not invent it and do not claim it. What
does not exist is a European place to run it, and that absence is the whole company.

## Page 3 · Technical maturity and why HPC

Technology Readiness Level 6: running with two Catalan municipalities under research
agreements, 340,000 documents, eleven live workspaces.

- **Trained models:** three fine-tuned encoders for Catalan and Spanish administrative text,
  plus a routing model that decides which part of a workspace a query needs — the component
  that makes narrow context loading work at archive scale.
- **Annotated datasets:** 41,000 archivist-confirmed record pairs and 12,000 filing-convention
  labels, annotated by working municipal archivists over eighteen months. To our knowledge the
  only labelled corpus of its kind for Catalan administrative records.
- **Validated algorithms:** routing reaches 0.91 macro-F1 on held-out workspaces; provenance
  reconstruction resolves 0.97 of citations to a specific file and version.

What we cannot do is serve inference at the scale of a region on hardware we can afford to
rent in Europe, which is precisely the constraint the AI Factory exists to remove. Access to
MareNostrum5 would let us do two things we have specified and cannot run: train one
cross-municipal routing model instead of one per archive, and benchmark open-weight serving
against the commercial APIs our customers are not allowed to call.

## Page 4 · Market and strategic relevance

There are 8,131 municipalities in Spain and roughly 90,000 public bodies in the Union. Every
one of them is being sold agentic AI, and every one of them is discovering the same thing at
the same point in procurement.

We sell per-workspace hosting with an annual support component, to the municipality or to the
regional body serving several. Two paid pilots to date. The buyer is usually not the
innovation office — it is the data-protection officer, who has been saying no for two years
and would prefer to say yes.

**We are not proposing to rebuild the American platforms in Europe.** They are good, they are
years ahead, and duplicating them would waste the head start the open methodology gave
everyone. The missing piece is narrower and duller: a European tier those platforms can hand a
workspace to when the customer is a public body — sovereign storage, sovereign inference,
sovereign audit trail, and nothing else different. The platform keeps the customer and the
product; the workspace simply runs on compute inside the jurisdiction.

That is what makes public HPC the right substrate rather than another commercial cloud. A
safeguarding tier whose guarantee rests on a commercial provider's regional pledge is back to
a promise; one that runs on infrastructure the Union itself funds and operates is a fact about
where the hardware is. EuroHPC is the only place in Europe where that sentence is true today,
which is the argument for building this here rather than anywhere else.

The strategic fit with the AI Factory is direct: this is AI applied to public administration,
built on European compute, where interpretability and residency are legal constraints rather
than preferences. It is also, plainly, an argument for European AI infrastructure having a
customer — if sovereign hosting has no product on top of it, it stays a research facility.

## Page 5 · Team and use of the Programme

Our staff: 14 engineers, 5 in operations, 3 in commercial. Two founders — an archivist of fourteen years and an ML engineer previously at
a Barcelona research group — plus the engineering and commercial staff above.

What we would use the Programme for, in order:

1. **Compute** — the cross-municipal routing model, specified and unrun.
2. **Serving** — benchmarking open-weight inference on EU hardware against the commercial
   APIs our customers cannot use, and publishing the comparison.
3. **Proximity** — the Barcelona site is where the Catalan language-resource groups are, and
   annotation is our bottleneck.

There is a pattern worth naming. The published methodology has produced a large body of
working folder-shaped systems, and only a small fraction of them are wired to anything a
non-author can actually use. The gap between a folder that works on its author's laptop and a
system an institution can adopt is not intelligence, and it is not method — it is hosting,
identity, versioning and a guarantee about where the bytes are. Those are unglamorous and
they are the entire adoption barrier for the one sector that most needs interpretable AI.

If the Programme wanted one sentence: the methodology for interpretable AI is already
published and already works. Europe is missing the place to run it, and that is a hosting
problem, not a research problem.

The CTO and one ML engineer will be on site four days a week.
