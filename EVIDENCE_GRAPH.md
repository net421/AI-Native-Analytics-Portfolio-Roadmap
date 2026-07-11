# Evidence Graph

The portfolio uses this traceability rule:

```text
Target role → skill → repository → concrete artifact → validation → safe claim
```

## Core graph

```mermaid
flowchart TD
    AE[Analytics Engineer] --> DBT[dbt Lab]
    AE --> CW[Cloud Warehouse]
    AI[AI-Native Analytics] --> SA[Semantic Agent]
    AI --> EV[Shared Evaluation]
    AI --> DT[Decision Twin]
    SC[Supply Chain / Operations] --> SCT[Control Tower]
    SC --> DT
    BI[BI Engineer] --> DASH[BI Dashboard Lab]
    GR[Growth Analyst] --> REV[Revenue Growth]
    EXP[Experimentation] --> CAUSAL[Causal Lab]

    CW --> V1[DB/export checks]
    DBT --> V2[101 dbt results]
    SA --> V3[Grounding, lineage, refusals]
    DT --> V4[Dify compatibility and scenario checks]
    EV --> V5[Shared fail-closed release]
    CAUSAL --> V6[Scientific reproduction and release envelope]
```

## Evidence quality rule

A strong claim requires all of the following:

1. a specific repository and artifact;
2. an executable or inspectable result;
3. a validation method;
4. an explicit limitation;
5. a recruiter or hiring-manager review path.

The release ledger records repository-level proof. Individual repositories document artifact-level evidence.
