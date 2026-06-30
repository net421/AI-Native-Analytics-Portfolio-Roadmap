# Repo Quality Standard

## Purpose

This standard defines what a repository in this analytics portfolio must demonstrate before it can be considered professionally credible.

The goal is not to create many repositories or many commits. The goal is to create strong, inspectable evidence for modern Data & Analytics Engineering, Analytics Engineering, BI Engineering, Supply Chain Analytics, Operations Analytics, Revenue/Growth Analytics, and AI-Augmented Data Workflow roles.

Each repository should answer four questions clearly:

1. What business or analytical problem does this repo address?
2. What technical skills does it prove?
3. What concrete files can a hiring manager inspect?
4. How is the work validated?

A repo should not look like a toy project, a prompt dump, or a generic AI-generated scaffold. It should look like a compact but serious portfolio project with clear business context, technical depth, validation discipline, and honest claim boundaries.

---

## Core Principle

Every artifact must map to visible job-market evidence.

A good artifact is not just a file. It should prove one or more of the following:

- advanced SQL ability
- analytics engineering judgment
- dbt-style modeling and testing
- Python analytics or pipeline ability
- cloud warehouse conceptual fluency
- BI/dashboard design skill
- data quality and validation discipline
- supply chain or operations analytics domain knowledge
- revenue/growth/product analytics thinking
- stakeholder communication
- AI-assisted execution with human validation

If an artifact does not improve evidence, clarity, validation, or technical credibility, it should not be added.

---

## Approved Portfolio Repositories

This standard applies first to these seven repositories:

1. `AI-Native-Analytics-Portfolio-Roadmap`
2. `cloud-warehouse-analytics-lab`
3. `dbt-analytics-engineering-lab`
4. `orchestration-data-pipelines-lab`
5. `tableau-bi-dashboard-lab`
6. `supply-chain-operations-control-tower`
7. `revenue-growth-analytics-engineering`

Older repositories should not be modified under this standard unless explicitly approved in a later phase.

---

## Repository Maturity Levels

### Level 0 — Empty or Placeholder

A repo is Level 0 if it has only a name, minimal README, empty folders, or placeholder files.

This level is not portfolio-ready.

### Level 1 — Scaffolded

A repo is Level 1 if it has:

- README
- folder structure
- basic explanation of purpose
- some initial files or docs

This is acceptable as a starting point, but not enough for professional evidence.

### Level 2 — Explained

A repo is Level 2 if it has:

- clear business problem
- target roles
- skills demonstrated
- repository structure
- AI-assisted workflow note
- limitations section

This is recruiter-readable but still needs stronger technical artifacts.

### Level 3 — Technical Evidence

A repo is Level 3 if it has inspectable artifacts such as:

- SQL scripts
- Python scripts
- dbt models
- schema tests
- dashboard specifications
- KPI dictionaries
- sample datasets
- validation plans
- architecture diagrams

This is the minimum level for a serious portfolio repo.

### Level 4 — Validated Evidence

A repo is Level 4 if it includes:

- validation logic
- expected outputs
- test/check descriptions
- data quality criteria
- assumptions
- known limitations
- reproducible run instructions

This is where the repo starts looking professionally credible.

### Level 5 — Hiring-Manager Ready

A repo is Level 5 if a technical reviewer can quickly understand:

- the business problem
- the architecture
- the data model
- the transformation logic
- the validation approach
- the skill evidence
- the limitations
- the next improvements

A Level 5 repo should feel like a compact real-world analytics project, not a demo folder.

---

## Minimum README Standard

Every serious repo should eventually include the following sections:

```text
# Project Title

## Executive Summary
## Business Problem
## Target Roles
## Skills Demonstrated
## Repository Structure
## Architecture
## Data Model or Analytical Model
## Key Metrics or Outputs
## Technical Artifacts
## Validation Strategy
## How to Review This Repo
## AI-Augmented Workflow
## Limitations
## Next Improvements
```

The README should not be vague. It should explain exactly what the repo proves and where to inspect the proof.

---

## Technical Evidence Standard

Each repo should contain at least three types of technical or semi-technical evidence.

### SQL Evidence

Strong SQL evidence includes:

- CTEs
- joins
- window functions
- aggregations
- date logic
- mart creation
- validation queries
- metric reconciliation
- platform-specific notes

Weak SQL evidence:

- one simple `SELECT *`
- generic example tables
- queries without business purpose
- queries with no validation

### Python Evidence

Strong Python evidence includes:

- clear input/output flow
- pandas transformations
- logging
- error handling
- validation checks
- CLI or runnable script structure
- comments explaining business rules
- expected output examples

Weak Python evidence:

- isolated toy functions
- no clear dataset
- no validation
- no run instructions
- code that does not map to a business problem

### dbt Evidence

Strong dbt evidence includes:

- `dbt_project.yml`
- staging models
- intermediate models
- marts
- `schema.yml`
- tests
- documentation
- lineage explanation
- source freshness or assumptions
- BI-ready final models

Weak dbt evidence:

- folders with no models
- models with no tests
- tests with no explanation
- unclear model grain
- no mart or business output

### BI Evidence

Strong BI evidence includes:

- KPI dictionary
- dashboard wireframe
- calculated fields
- stakeholder questions
- filter logic
- metric definitions
- data source assumptions
- validation criteria
- Tableau/Looker/Sigma-ready documentation

Weak BI evidence:

- generic chart list
- screenshots without definitions
- metrics with no formulas
- dashboard without business decisions

### Orchestration Evidence

Strong orchestration evidence includes:

- DAG/flow/asset examples
- dependency explanation
- retry strategy
- logging
- failure handling
- idempotency notes
- monitoring notes
- validation gates

Weak orchestration evidence:

- tool names only
- no dependency flow
- no error handling
- no operational assumptions

---

## Validation Standard

Each repo should answer these validation questions:

1. What is the expected grain of the output?
2. Which keys must be unique?
3. Which fields must not be null?
4. Which accepted values are allowed?
5. Which totals should reconcile?
6. Which edge cases could break the logic?
7. What assumptions affect interpretation?
8. What limitations should be disclosed?

Validation can be implemented through:

- SQL validation queries
- dbt tests
- Python checks
- pytest
- data quality scripts
- documented expected outputs
- CI checks
- manual review checklists

A repo without validation should not claim strong analytical reliability.

---

## Claim Boundary Standard

The portfolio must avoid fake enterprise claims.

Use safe language:

- “Snowflake-style SQL patterns”
- “BigQuery-ready analytical SQL”
- “DuckDB local warehouse simulation”
- “dbt-style analytics engineering lab”
- “Tableau-ready dashboard specification”
- “Airflow orchestration example”
- “Azure Data Factory pipeline design pattern”
- “human-validated AI-assisted workflow”
- “synthetic ERP/WMS/TMS-style data”

Avoid unsafe language unless fully supported:

- “production Snowflake deployment”
- “enterprise Databricks implementation”
- “real client data”
- “production control tower”
- “expert in every tool”
- “fully automated analytics system”

The correct message is:

> I can use AI-native execution to build, validate, and document modern analytics workflows while maintaining human control over business logic, assumptions, quality, and final claims.

---

## Hiring Signal Rubric

Each repo should be scored from 0 to 5 across these dimensions.

| Dimension | 0 | 3 | 5 |
|---|---|---|---|
| Business clarity | unclear | understandable problem | strong real-world framing |
| Technical depth | placeholders | some artifacts | inspectable technical work |
| Validation | none | documented checks | executable or well-defined checks |
| Role alignment | unclear | maps to one role | maps to multiple target roles |
| Recruiter readability | confusing | readable | clear and compelling |
| Hiring manager credibility | toy-like | decent lab | serious portfolio evidence |
| Claim discipline | exaggerated | mostly safe | precise and honest |
| AI-native workflow | absent | mentioned | clearly documented and validated |

A repo should target an average score of at least 4 before being promoted as a primary pinned portfolio project.

---

## Repository-Specific Quality Targets

### `cloud-warehouse-analytics-lab`

Must demonstrate:

- Snowflake-style SQL
- BigQuery-ready SQL
- Databricks/lakehouse concepts
- Redshift/Synapse comparison
- DuckDB local simulation
- validation queries
- warehouse design and performance notes

Minimum professional artifacts:

- cloud warehouse comparison document
- SQL mart examples
- partitioning/clustering notes
- semi-structured data example
- local DuckDB pipeline
- validation plan

### `dbt-analytics-engineering-lab`

Must demonstrate:

- staging models
- intermediate models
- marts
- schema tests
- documentation
- lineage
- BI-ready outputs

Minimum professional artifacts:

- `dbt_project.yml`
- `models/staging/`
- `models/intermediate/`
- `models/marts/`
- `schema.yml`
- lineage notes
- validation notes
- model grain documentation

### `orchestration-data-pipelines-lab`

Must demonstrate:

- Airflow DAG thinking
- Prefect flow thinking
- Dagster asset thinking
- ADF pipeline design
- SSIS concept mapping
- retries, logging, error handling

Minimum professional artifacts:

- one DAG example
- one Prefect flow
- retry pattern document
- logging utility
- failure handling explanation
- monitoring checklist

### `tableau-bi-dashboard-lab`

Must demonstrate:

- Tableau calculated fields
- dashboard wireframes
- KPI definitions
- semantic layer thinking
- Looker/Sigma alternatives
- stakeholder-driven design

Minimum professional artifacts:

- calculated fields document
- executive dashboard wireframe
- KPI dictionary
- LookML-style examples
- self-service BI notes
- dashboard validation checklist

### `supply-chain-operations-control-tower`

Must demonstrate:

- ERP/WMS/TMS-style analytics
- OTIF
- fill rate
- inventory turnover
- days of inventory
- lead time
- stockouts
- backorders
- freight cost
- service level
- stakeholder summary

Minimum professional artifacts:

- synthetic data
- KPI dictionary
- SQL KPI logic
- Python KPI script
- validation checks
- dashboard specification
- executive summary

### `revenue-growth-analytics-engineering`

Must demonstrate:

- funnel analytics
- cohort analysis
- retention
- churn
- customer segmentation
- revenue segmentation
- growth dashboard logic
- stakeholder interpretation

Minimum professional artifacts:

- funnel SQL
- cohort SQL
- retention/churn logic
- segmentation Python
- stakeholder summary
- validation plan
- dashboard spec

### `AI-Native-Analytics-Portfolio-Roadmap`

Must demonstrate:

- strategic portfolio organization
- skill coverage matrix
- backlog
- evidence map
- role mapping
- quality standard
- AI workflow playbook
- recruiter guide

Minimum professional artifacts:

- `SKILL_COVERAGE_MATRIX.md`
- `PORTFOLIO_EVIDENCE.md`
- `BACKLOG.md`
- `JOB_TARGETS.md`
- `REPO_QUALITY_STANDARD.md`
- `AI_WORKFLOW_PLAYBOOK.md`
- `RECRUITER_GUIDE.md`

---

## Definition of Done for Any Improvement

A change is done only if it meets these criteria:

1. It improves a real skill signal.
2. It modifies or adds meaningful content.
3. It maps to a target role.
4. It includes or improves validation.
5. It avoids exaggerated claims.
6. It improves recruiter or hiring-manager readability.
7. It has a clear suggested commit message.
8. It does not add duplicate fluff.
9. It does not create disconnected artifacts.
10. It makes the repo more credible than before.

---

## Suggested Commit Message Format

Use clear messages such as:

- Add dbt schema tests and lineage notes
- Expand Snowflake-style warehouse SQL examples
- Add BigQuery nested data and partitioning examples
- Add Airflow orchestration pattern with retry notes
- Add Tableau dashboard KPI specification
- Add supply chain KPI validation checks
- Add revenue cohort analysis model
- Improve recruiter-facing evidence map
- Add repository quality standard

Avoid:

- update files
- changes
- more stuff
- fix
- AI update
- misc improvements

---

## Codex Implementation Rules

When Codex works on a repo, it should follow this loop:

1. Inspect the repo.
2. Identify the weakest high-impact evidence gap.
3. Select exactly one focused improvement.
4. Implement concrete files or edits.
5. Update documentation explaining what skill improved.
6. Add validation criteria or checks.
7. Avoid fake claims.
8. Run available checks if possible.
9. Summarize files changed.
10. Suggest the next best task.

Codex should not:

- create random repos
- add empty folders
- generate generic README fluff
- make unsupported production claims
- modify older repos without explicit permission
- make large changes without explaining risk

---

## Final Portfolio Standard

The end-state portfolio should communicate:

> This is a deliberate, coverage-driven analytics portfolio demonstrating SQL, Python, dbt, cloud warehouse concepts, BI/dashboard design, orchestration, data quality, CI/CD, supply chain analytics, revenue analytics, stakeholder storytelling, and AI-native analytical execution with human validation.

Every repo should support that sentence with concrete, inspectable evidence.
