# Cartulary — Executive Summary

*BSC AI Factory Incubation Programme, Call 3. Submitted 2026-09-08.*
*Length as submitted: **5 pages** (PDF, A4). FICTIONAL — see README.md.*

---

## Page 1 · The problem

Agentic AI has a working architecture for knowledge work, and European freight operators
cannot trust it with their dispatch floor.

The architecture is interpretable context methodology: instead of hiding a process inside
model weights or framework code, you express it as a folder of plain files a person can read
— what the agent is, what rules it follows, what it may and may not load at each step. One
model walks the structure. A dispatcher can open any folder and see exactly what the system
was told. For freight this is not a nicety; when a load is rerouted, refused or delivered late,
the operator has to explain to the shipper and the carrier why, and a folder can be read in a
way an embedding cannot.

The platforms that host these workspaces are American. That places the workspace — which for
a road-freight operator holds consignment notes, shipper contracts, rate agreements and the
reasoning applied to them — on infrastructure the operator does not control, next to the
commercial data of its competitors' platforms. Shippers write data-location clauses into
their contracts, and the largest of them audit those clauses. The outcome is predictable:
pilots that never leave the sandbox, tenders that stall at the shipper's security review, and
a working methodology adopted everywhere except the operators whose margins most depend on
getting dispatch right.

The methodology is not the gap. The hosting is.

## Page 2 · What we build

Cartulary is European hosting for interpretable context workspaces: the same folder-shaped
architecture, run entirely on European infrastructure, with the guarantees a freight operator
has to be able to write into a shipper contract.

Three things, none of which is a model:

1. **Location with proof.** Every workspace, every document and every inference stays in the
   EU. Not a statement of intent — a per-request log a shipper's security team can audit, naming
   which node served it.
2. **The folder is the record.** Because the workspace is plain files, the archive of what the
   agent was told is the workspace itself, versioned. When a delivery dispute reaches a claim
   months later, the exact context that produced the dispatch decision can be reconstructed and
   read.
3. **Inference on EU compute.** Open-weight models served from European hardware, so the
   location guarantee survives the part where the work actually happens.

### Why this is infrastructure and not a promise

A data-location promise written into a service agreement is a request. A location guarantee
enforced by the fact that no node outside the Union can serve the request is a constraint.
Large shippers have learned to tell the difference, which is why so many pilots die at the
security review: the vendor offers the first and the reviewer needs the second.

The same distinction shapes the product. An interpretable workspace already separates the
part the operator owns — its loads, its documents, its dispatch decisions — from the part the
platform maintains. Hosting that split is the whole job: the operator's half never leaves the
jurisdiction, the platform's half updates underneath it, and neither can silently absorb the
other. We hold the split as a hard boundary rather than a convention, because a convention is
something an upgrade can quietly cross.

And because the workspace is files under version control, it accretes. The record of what the
system was told is not a log written beside the work — it *is* the work, at every past
version. A dispatch decision disputed next season is reconstructed by checking out the
workspace as it stood, not by trusting a description of it.

The methodology is published and open (Van Clief & McDermott, *Folder Structure as Agentic
Architecture*, arXiv:2603.16021, MIT-licensed). We did not invent it and do not claim it. What
does not exist is a European place to run it for freight, and that absence is the whole
company.

## Page 3 · Technical maturity and why HPC

Technology Readiness Level 6: running with two Catalan road-freight operators under pilot
agreements, 340,000 documents, eleven live workspaces.

- **Trained models:** three fine-tuned encoders for Catalan and Spanish consignment notes and
  delivery records, plus a routing model that decides which part of a workspace a query needs
  — the component that makes narrow context loading work at fleet scale.
- **Annotated datasets:** 41,000 dispatcher-confirmed shipment-record pairs and 12,000
  delivery-exception labels, annotated by working dispatchers over eighteen months. To our
  knowledge the only labelled corpus of its kind for Iberian road-freight documents.
- **Validated algorithms:** routing reaches 0.91 macro-F1 on held-out workspaces; provenance
  reconstruction resolves 0.97 of citations to a specific file and version.

What we cannot do is serve inference at the scale of a national fleet on hardware we can
afford to rent in Europe, which is precisely the constraint the AI Factory exists to remove.
Access to MareNostrum5 would let us do two things we have specified and cannot run: train one
cross-operator routing model instead of one per operator, and benchmark open-weight serving
against the commercial APIs our customers' shippers will not let them call.

## Page 4 · Market and strategic relevance

Road carries most of the Union's inland freight, and the operators behind it are
overwhelmingly small. Every one of them is being sold agentic AI, and every one of them hits the same wall at the same point in a shipper's
tender.

We sell per-workspace hosting with an annual support component, to the operator or to the
logistics group serving several. Two paid pilots to date. The buyer is usually not the
operations director — it is the person answering the shipper's security questionnaire, who
has been saying no for two years and would prefer to say yes.

**We are not proposing to rebuild the American platforms in Europe.** They are good, they are
years ahead, and duplicating them would waste the head start the open methodology gave
everyone. The missing piece is narrower and duller: a European tier those platforms can hand a
workspace to when the customer's shipper requires it — European storage, European inference,
European audit trail, and nothing else different. The platform keeps the customer and the
product; the workspace simply runs on compute inside the jurisdiction.

That is what makes European HPC the right substrate rather than another commercial cloud. A
tier whose guarantee rests on a commercial provider's regional pledge is back to a promise;
one that runs on infrastructure located and operated in the Union is a fact about where the
hardware is.

The strategic fit with the AI Factory is indirect: this is AI applied to freight logistics,
built on European compute, where explainability and data location are contractual demands
rather than preferences. It is also, plainly, an argument for European AI infrastructure
having a commercial customer outside research.

## Page 5 · Team and use of the Programme

Seven people. Two founders — a freight dispatcher of fourteen years and an ML engineer
previously at a Barcelona research group — plus three ML engineers, one backend engineer and one
part-time commercial lead. Five are technical.

What we would use the Programme for, in order:

1. **Compute** — the cross-operator routing model, specified and unrun.
2. **Serving** — benchmarking open-weight inference on EU hardware against the commercial
   APIs our customers cannot use, and publishing the comparison.
3. **Proximity** — the Barcelona site is where the Catalan language-resource groups are, and
   annotation is our bottleneck.

There is a pattern worth naming. The published methodology has produced a large body of
working folder-shaped systems, and only a small fraction of them are wired to anything a
non-author can actually use. The gap between a folder that works on its author's laptop and a
system a freight operator can adopt is not intelligence, and it is not method — it is hosting,
identity, versioning and a guarantee about where the bytes are. Those are unglamorous and they
are the entire adoption barrier for the operators who most need dispatch they can explain.

If the Programme wanted one sentence: the methodology for interpretable AI is already
published and already works. European freight is missing the place to run it, and that is a
hosting problem, not a research problem.

The CTO and one ML engineer will be on site four days a week.
