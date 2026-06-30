# AI Hiring Readability Standard

## Purpose

This standard defines how the portfolio should be structured so that it can be read clearly by:

- AI hiring assistants
- ATS-style screening systems
- technical recruiters
- sourcers
- hiring managers
- technical interviewers
- human reviewers scanning quickly

The goal is not keyword stuffing. The goal is structured, honest, machine-readable and human-readable evidence.

A reviewer should be able to answer these questions quickly:

1. What roles is this portfolio targeting?
2. What skills are demonstrated?
3. Which repository proves each skill?
4. Which specific file or artifact proves the claim?
5. How was the artifact validated?
6. What claims are safe to make?
7. What claims are only lab/simulation evidence?

---

## Core Principle

Every important skill claim should resolve to a concrete artifact.

Bad pattern:

> Skilled in Snowflake, dbt, Tableau, Airflow, supply chain analytics, and revenue analytics.

Better pattern:

> Snowflake-style SQL patterns are demonstrated in `cloud-warehouse-analytics-lab/snowflake/sql/analytics_mart_patterns.sql`.
>
> dbt-style staging, intermediate, mart, and schema test patterns are demonstrated in `dbt-analytics-engineering-lab/models/`.
>
> Tableau-ready dashboard specifications are demonstrated in `tableau-bi-dashboard-lab/tableau/dashboard_wireframes/`.

A hiring AI or recruiter should not need to guess where the evidence is.

---

## Portfolio Reading Path

The portfolio should be readable in this order:

```text
GitHub profile README
  -> AI-Native-Analytics-Portfolio-Roadmap
  -> SKILL_COVERAGE_MATRIX.md
  -> PORTFOLIO_EVIDENCE.md
  -> JOB_TARGETS.md
  -> individual evidence repos
  -> technical files
  -> validation docs
```

This creates a guided path from high-level positioning to inspectable technical proof.

---

## Required Central Files

The central roadmap repo should include:

```text
README.md
SKILL_COVERAGE_MATRIX.md
PORTFOLIO_EVIDENCE.md
JOB_TARGETS.md
REPO_QUALITY_STANDARD.md
AI_HIRING_READABILITY_STANDARD.md
AI_WORKFLOW_PLAYBOOK.md
RECRUITER_GUIDE.md
BACKLOG.md
```

Each file has a different purpose.

| File | Purpose |
|---|---|
| `README.md` | high-level narrative and entry point |
| `SKILL_COVERAGE_MATRIX.md` | skill-to-repo map |
| `PORTFOLIO_EVIDENCE.md` | skill-to-artifact map |
| `JOB_TARGETS.md` | role-to-evidence map |
| `REPO_QUALITY_STANDARD.md` | quality bar for all repos |
| `AI_HIRING_READABILITY_STANDARD.md` | machine/human readability rules |
| `AI_WORKFLOW_PLAYBOOK.md` | AI-assisted execution methodology |
| `RECRUITER_GUIDE.md` | how recruiters should scan the portfolio |
| `BACKLOG.md` | what is being improved next |

---

## GitHub Profile README Standard

The GitHub profile README should act as the top-level router.

It should include:

1. One-sentence professional positioning.
2. Target role families.
3. Core skill clusters.
4. Link to central roadmap repo.
5. Link to skill coverage matrix.
6. Link to strongest evidence repos.
7. Clear explanation that the portfolio is coverage-driven.
8. No exaggerated claims.
9. No long walls of text before the evidence links.

Recommended structure:

```markdown
# Data & Analytics Engineering Portfolio

I build analytics engineering, BI, operations analytics, supply chain analytics, revenue analytics, and AI-assisted data workflow projects using SQL, Python, dbt-style modeling, BI specifications, validation checks, and stakeholder-facing documentation.

## Portfolio Evidence System

This GitHub is organized as a coverage-driven evidence system.

Start here:
- [Portfolio Roadmap](...)
- [Skill Coverage Matrix](...)
- [Portfolio Evidence Map](...)
- [Recruiter Guide](...)

## Strongest Evidence Repos

| Skill Area | Repository | Evidence |
|---|---|---|
| dbt / Analytics Engineering | ... | staging, marts, tests, lineage |
| Cloud Warehouse SQL | ... | Snowflake-style, BigQuery-ready, DuckDB simulation |
| Supply Chain Analytics | ... | OTIF, fill rate, lead time, stockouts |
| BI / Tableau | ... | KPI dictionary, dashboard specs |
| Revenue Analytics | ... | funnel, cohort, retention |
```

The profile README should not try to explain everything. Its job is to route the reader.

---

## Skill Coverage Matrix Standard

The skill matrix should be easy for AI and humans to parse.

Required columns:

```text
Skill
Evidence Repository
Specific Artifact
Status
Claim Level
Target Roles
Validation
Next Improvement
```

Example:

| Skill | Evidence Repository | Specific Artifact | Status | Claim Level | Target Roles | Validation | Next Improvement |
|---|---|---|---|---|---|---|---|
| dbt analytics engineering | `dbt-analytics-engineering-lab` | `models/schema.yml`, `models/marts/fct_orders.sql` | In progress | Lab evidence | Analytics Engineer | schema tests documented | add singular data test |
| Snowflake-style SQL | `cloud-warehouse-analytics-lab` | `snowflake/sql/analytics_mart_patterns.sql` | In progress | Pattern evidence | Data Engineer, Analytics Engineer | validation queries | add cost/performance examples |
| Supply chain KPIs | `supply-chain-operations-control-tower` | `kpis/kpi_dictionary.md`, `sql/supply_chain_kpis.sql` | In progress | Simulation evidence | Supply Chain Analyst | synthetic data checks | add output examples |

---

## Claim Level Standard

Each skill should have a clear claim level.

Use one of these:

| Claim Level | Meaning |
|---|---|
| `Strong evidence` | repo has technical artifacts, docs, validation, and clear review path |
| `Lab evidence` | repo demonstrates a realistic lab or simulation |
| `Pattern evidence` | repo demonstrates transferable concepts or design patterns |
| `Planned evidence` | skill is planned but not yet demonstrated |
| `Weak evidence` | some mention exists, but proof is incomplete |

This prevents overclaiming.

---

## Machine-Readable Evidence Pattern

Use consistent phrases across repos.

Preferred language:

- `Skills demonstrated`
- `Target roles`
- `Business problem`
- `Technical artifacts`
- `Validation strategy`
- `How to review this repo`
- `Limitations`
- `AI-augmented workflow`
- `Claim boundary`

These headings help both humans and automated systems identify relevant evidence.

Avoid vague headings like:

- `Stuff`
- `Notes`
- `Misc`
- `Experiments`
- `Random ideas`

---

## Recommended Evidence Map Format

Each repo should include or link to an evidence map.

Example:

```markdown
# Evidence Map

| Skill | File | What It Proves | Validation |
|---|---|---|---|
| Advanced SQL | `sql/funnel_analysis.sql` | CTEs, joins, conversion logic | output count checks |
| Data quality | `validation/checks.py` | null, duplicate, accepted value checks | script output |
| Stakeholder communication | `stakeholder_summary/summary.md` | business interpretation | reviewed assumptions |
```

This makes the portfolio easier to parse.

---

## Repository README Standard for AI Readability

Every repo README should include these exact or near-exact sections:

```markdown
## Executive Summary
## Business Problem
## Target Roles
## Skills Demonstrated
## Repository Structure
## Architecture
## Data Model
## Technical Artifacts
## Validation Strategy
## How to Review This Repo
## What This Demonstrates for Hiring Managers
## AI-Augmented Workflow
## Limitations
## Next Improvements
```

The most important section for hiring systems is:

```markdown
## What This Demonstrates for Hiring Managers
```

This section should explicitly connect the repo to job evidence.

Example:

```markdown
This project demonstrates that I can transform raw operational data into governed, validated, BI-ready analytical outputs using SQL, Python, KPI definitions, dashboard specifications, and stakeholder-facing documentation.
```

---

## Artifact Naming Standard

File names should be descriptive.

Good:

```text
analytics_mart_patterns.sql
cohort_retention.sql
supply_chain_kpis.sql
schema.yml
validation_plan.md
kpi_dictionary.md
executive_dashboard_wireframe.md
recruiter_review_guide.md
```

Weak:

```text
test.sql
stuff.py
notes.md
newfile.md
demo.py
analysis2.sql
```

Descriptive names help automated readers understand the artifact before opening it.

---

## Cross-Linking Standard

Every repo should link back to the central roadmap.

Add this near the top or bottom of each README:

```markdown
## Portfolio Context

This repository is part of the AI-Native Analytics Portfolio, a coverage-driven evidence system for modern Data & Analytics Engineering roles.

Start with the central roadmap:
[AI-Native-Analytics-Portfolio-Roadmap](https://github.com/net421/AI-Native-Analytics-Portfolio-Roadmap)
```

The central roadmap should link outward to all seven repos.

This creates a graph rather than isolated projects.

---

## Target Role Mapping Standard

The portfolio should map evidence to roles.

Example:

| Target Role | Evidence Repos | Strongest Signals |
|---|---|---|
| Analytics Engineer | `dbt-analytics-engineering-lab`, `cloud-warehouse-analytics-lab` | dbt models, marts, schema tests, SQL |
| BI Engineer | `tableau-bi-dashboard-lab`, `supply-chain-operations-control-tower` | KPI dictionary, dashboard specs, semantic layer |
| Supply Chain Analyst | `supply-chain-operations-control-tower` | OTIF, fill rate, lead time, stockout analytics |
| Growth Analyst | `revenue-growth-analytics-engineering` | funnel, cohort, retention, segmentation |
| Data Engineer | `orchestration-data-pipelines-lab`, `cloud-warehouse-analytics-lab` | pipelines, orchestration, validation, warehouse design |

---

## Keyword Strategy Without Keyword Stuffing

Important tool and skill terms should appear naturally in context.

Good:

> This repo includes Snowflake-style SQL patterns, BigQuery-ready nested data examples, Databricks lakehouse notes, and a DuckDB local simulator to demonstrate cloud warehouse modeling concepts.

Bad:

> Snowflake BigQuery Databricks Redshift Synapse SQL warehouse cloud cloud cloud analytics analytics analytics.

The portfolio should be searchable, but not spammy.

---

## AI-Augmented Workflow Standard

Every relevant repo should include:

```markdown
## AI-Augmented Workflow

This project was developed using an AI-native analytics workflow. AI was used to accelerate code generation, SQL drafting, documentation, dashboard specification, validation planning, and iteration.

The analytical framing, KPI definitions, assumptions, validation criteria, and final review remain human-directed.

Workflow:
1. Define the business problem.
2. Define metrics and assumptions.
3. Generate technical artifacts using AI-assisted iteration.
4. Validate outputs against expected logic.
5. Document limitations and claim boundaries.
6. Package the result as recruiter-readable portfolio evidence.
```

This turns AI usage into a strength rather than a hidden concern.

---

## Validation Visibility Standard

Validation should be visible without running code.

Every repo should ideally include:

```text
validation/
  validation_plan.md
  expected_checks.md
  sample_validation_output.md
```

Even if code is not executed by a reviewer, they should see how correctness would be assessed.

---

## Recruiter Review Guide Standard

Each serious repo should include a short recruiter guide.

Example:

```markdown
# Recruiter Review Guide

## Best 60-Second Review Path

1. Read the Executive Summary.
2. Review the Skills Demonstrated table.
3. Open the Evidence Map.
4. Inspect one technical artifact.
5. Read the Validation Strategy.

## Best Technical Review Path

1. Inspect the data model.
2. Review SQL/Python/dbt artifacts.
3. Review validation checks.
4. Read limitations.
5. Review next improvements.
```

This is useful because many reviewers scan quickly.

---

## Anti-Toy-Repo Checklist

Before promoting a repo, check:

- Does it solve a believable business problem?
- Does it include inspectable technical artifacts?
- Does it include validation?
- Does it have realistic data or a documented simulation?
- Does it explain limitations?
- Does it map to target roles?
- Does it link back to the central roadmap?
- Does it avoid fake production claims?
- Does it contain more than generic README language?
- Can someone understand its value in under 60 seconds?

If the answer is no to more than two, the repo needs more work.

---

## Ideal Repo Summary Block

Each repo README should include a summary block like this:

```markdown
## Evidence Summary

| Category | Evidence |
|---|---|
| Business problem | Operational KPI control tower for ERP/WMS/TMS-style data |
| Main skills | SQL, Python, KPI design, validation, dashboard specification |
| Technical artifacts | `sql/`, `python/`, `kpis/`, `validation/` |
| Target roles | Supply Chain Analyst, Operations Analyst, Analytics Engineer |
| Claim level | Synthetic data portfolio simulation |
| Validation | KPI checks, null checks, reconciliation notes |
```

This is extremely readable for AI and humans.

---

## Final Standard

The portfolio should communicate this message:

> My GitHub is organized as a deliberate, coverage-driven evidence system for modern analytics roles. It demonstrates SQL, Python, dbt, cloud warehouse concepts, BI/dashboard design, orchestration, data quality, supply chain analytics, revenue analytics, stakeholder storytelling, and AI-native execution with human validation.

Every repo should support that statement with specific files, clear links, validation notes, and honest claims.
