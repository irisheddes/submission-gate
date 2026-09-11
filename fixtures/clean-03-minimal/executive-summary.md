# Cartulary — Executive Summary

*BSC AI Factory Incubation Programme, Call 3. Submitted 2026-09-08.*
*Length as submitted: **2 pages** (PDF, A4). FICTIONAL — see README.md.*

---

## Page 1 · What we do and why it needs HPC

Cartulary hosts interpretable AI workspaces on European infrastructure for public bodies that
cannot legally place case files on third-country platforms. The methodology is published and
open (Van Clief & McDermott, arXiv:2603.16021); the European place to run it is what is
missing.

We are at Technology Readiness Level 6, live with two Catalan municipalities under research
agreements across 340,000 documents. We have trained three encoders for Catalan and Spanish
administrative text and a routing model that decides which part of a workspace a query needs;
we hold 41,000 archivist-confirmed record pairs and 12,000 filing-convention labels, annotated
over eighteen months. Routing reaches 0.91 macro-F1 on held-out workspaces.

What we cannot do on rentable European hardware is serve inference at regional scale, or train
one cross-municipal routing model instead of one per archive. That is the specific constraint
MareNostrum5 removes.

## Page 2 · Market, team, and the ask

8,131 municipalities in Spain; roughly 90,000 public bodies in the Union. Each is being sold
agentic AI and each stops at the same point in procurement. We sell per-workspace hosting with
annual support, to the municipality or the regional body serving several. Two paid pilots.

Nineteen people, twelve technical. Two founders — an archivist of fourteen years and an ML
engineer from a Barcelona research group.

We would use the Programme for compute, for benchmarking open-weight serving on EU hardware
against the commercial APIs our customers may not call, and for proximity to the Catalan
language-resource groups, since annotation is our bottleneck.

Three of us will be on site three days a week.
