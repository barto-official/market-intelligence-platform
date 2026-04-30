# Request for Comments (RFCs)

**Request for Comments (RFCs)** are structured design proposals used to discuss, review, and converge on significant technical changes *before* (or alongside) implementation.

RFCs are the primary mechanism for **early alignment and design review**. They complement Architecture Decision Records (ADRs), which capture the final, long-lived decisions that result from accepted RFCs.

______________________________________________________________________

## What is an RFC?

An RFC is a proposal document that describes:

- the problem being solved,
- the relevant constraints and requirements,
- one or more viable design options,
- the trade-offs and risks involved,
- and a recommended direction.

RFCs are intended to be reviewed asynchronously and iterated on through feedback. They are not final decision records.

______________________________________________________________________

## When to write an RFC

The same rules applies as for ADR. Write an RFC when a change is:

- cross-cutting (affects multiple modules/services/teams),
- impacts interfaces or dependencies
- hard or expensive to reverse,
- contract-defining (APIs, events, data schemas),
- operationally risky (security, reliability, scalability),
- or non-obvious with multiple reasonable alternatives.

Do **not** write RFCs for small local refactors or routine implementation details.

______________________________________________________________________

## RFCs vs ADRs

| RFC                        | ADR                            |
| -------------------------- | ------------------------------ |
| Proposal and discussion    | Final decision record          |
| Exploratory and mutable    | Stable and long-lived          |
| May include open questions | No open questions              |
| Used *before* commitment   | Used *after* decision          |
| Drives alignment           | Preserves architectural memory |

**Rule:**
Accepted RFCs must result in one or more ADRs capturing the final decisions.

______________________________________________________________________

## Key principles

- RFCs exist to enable **better decisions, earlier**.
- Discussion belongs in Issues; conclusions belong in documents.
- ADRs preserve decisions; RFCs explore them.
- Prefer clarity and explicit trade-offs over premature certainty.

______________________________________________________________________

## Where RFCs live

- RFCs are stored in-repo as Markdown files under `docs/rfc/`. It also includes template file.
- Filenames follow the pattern: `NNNN-kebab-case-title.md`.
- The RFC document is the **source of truth**.

______________________________________________________________________

## Workflow (hybrid model)

1. **Create RFC (Draft)**
   Copy the RFC template and create `docs/rfc/NNNN-title.md`.

1. **Open discussion (optional but recommended)**
   Create a GitHub Issue that links to the RFC for comments and feedback.

1. **Review and iterate**
   Update the RFC document to reflect conclusions from discussion.

1. **Decision**
   Update RFC status to `Accepted` or `Rejected`.
   Record the decision and rationale in the RFC.

1. **Create ADR(s) through PR**
   For accepted RFCs, create ADR(s) capturing the final decisions

1. **Close discussion**
   Close the GitHub Issue once the RFC is resolved.

______________________________________________________________________

## RFC status lifecycle

Typical statuses:

- `Draft`
- `In Review`
- `Accepted`
- `Rejected`
- `Implemented`
- `Superseded`
