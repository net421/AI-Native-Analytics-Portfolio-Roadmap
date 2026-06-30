# Hiring Signal Rubric

## Purpose

This rubric defines how each repository in the analytics portfolio should be evaluated before it is promoted as strong evidence for hiring.

The goal is to prevent the portfolio from becoming a set of toy repositories, generic README files, or disconnected AI-generated artifacts. Each repo should produce clear, inspectable, validated evidence for specific target roles.

This rubric is designed for:

- self-review
- Codex implementation review
- ChatGPT portfolio review loops
- recruiter-facing portfolio refinement
- hiring-manager readability
- AI-assisted hiring screeners

---

## Core Evaluation Question

Every repository should answer this question:

> If a recruiter, hiring manager, or AI hiring assistant scans this repository, what specific job-relevant evidence will they find?

A repository is strong only when the answer points to concrete artifacts, not vague claims.

---

## Scoring Scale

Use a 0 to 5 score for each dimension.

| Score | Meaning |
|---|---|
| 0 | Missing or not demonstrated |
| 1 | Mentioned but not supported |
| 2 | Basic scaffold or weak evidence |
| 3 | Understandable and partially useful |
| 4 | Strong, inspectable evidence |
| 5 | Hiring-manager ready evidence |

A repo should average **4.0+** before being treated as a flagship portfolio project.

---

## Rubric Dimensions

### 1. Business Clarity

| Score | Criteria |
|---|---|
| 0 | No business problem |
| 1 | Generic topic only |
| 2 | Basic business context |
| 3 | Clear use case with target users |
| 4 | Strong business framing with metrics and decisions |
| 5 | Realistic domain framing, stakeholders, tradeoffs, and decision impact |

Questions to ask:

- What business problem does the repo solve?
- Who would use the output?
- What decision does the analysis support?
- Which KPIs or operational outcomes matter?

---

### 2. Technical Depth

| Score | Criteria |
|---|---|
| 0 | No technical artifact |
| 1 | Placeholder files only |
| 2 | Simple examples with limited logic |
| 3 | Some real SQL, Python, dbt, BI, or orchestration artifacts |
| 4 | Multiple inspectable artifacts with realistic logic |
| 5 | Strong technical implementation with architecture, transformations, validation, and documentation |

Strong technical evidence may include:

- advanced SQL
- dbt models and tests
- Python pipelines
- orchestration examples
- KPI logic
- semantic layer definitions
- dashboard specifications
- CI checks
- validation scripts

---

### 3. Evidence Specificity

| Score | Criteria |
|---|---|
| 0 | No evidence map |
| 1 | Claims without file paths |
| 2 | Some artifacts but hard to connect to skills |
| 3 | Skills and files are partially mapped |
| 4 | Most claims link to concrete files |
| 5 | Every major skill claim resolves to a specific artifact and validation method |

Preferred pattern:

```text
Skill -> Repository -> File -> What it proves -> Validation -> Claim level
```

Example:

```text
dbt analytics engineering -> dbt-analytics-engineering-lab -> models/marts/fct_orders.sql -> mart modeling and grain definition -> schema.yml tests -> lab evidence
```

---

### 4. Validation Discipline

| Score | Criteria |
|---|---|
| 0 | No validation |
| 1 | Mentions validation but no details |
| 2 | Manual checks only |
| 3 | Validation plan or basic checks |
| 4 | SQL/dbt/Python checks documented or executable |
| 5 | Clear validation strategy with expected outputs, edge cases, assumptions, and limitations |

Validation should answer:

- What should be unique?
- What should not be null?
- What totals should reconcile?
- What accepted values are allowed?
- What assumptions are being made?
- What could break the analysis?
- How would the reviewer verify correctness?

---

### 5. Role Alignment

| Score | Criteria |
|---|---|
| 0 | No target role |
| 1 | Generic "data" role mention |
| 2 | One role loosely connected |
| 3 | Clear target role mapping |
| 4 | Multiple role mappings with evidence |
| 5 | Role-specific evidence paths for recruiters and hiring managers |

Target role families:

- Analytics Engineer
- Data & Analytics Engineer
- BI Analyst / BI Engineer
- Data Analyst
- Senior Data Analyst
- Supply Chain Analyst
- Operations Analyst
- Revenue / Growth Analyst
- Product Analyst
- Analytics Consultant
- AI-Augmented Data Workflow Specialist

---

### 6. Recruiter Readability

| Score | Criteria |
|---|---|
| 0 | Hard to understand quickly |
| 1 | Long text with unclear value |
| 2 | Basic README but weak navigation |
| 3 | Clear summary and skills |
| 4 | Strong 60-second review path |
| 5 | Recruiter can quickly understand target roles, strongest artifacts, and safe claims |

A strong repo should include:

- executive summary
- target roles
- skills demonstrated
- evidence summary table
- how to review this repo
- limitations
- central roadmap link

---

### 7. Hiring Manager Credibility

| Score | Criteria |
|---|---|
| 0 | Looks empty or unserious |
| 1 | Looks like a prompt dump |
| 2 | Looks like a beginner demo |
| 3 | Looks like a credible lab |
| 4 | Looks like serious portfolio evidence |
| 5 | Looks like a compact professional analytics case study |

A hiring manager should see:

- realistic problem framing
- technical artifacts
- thoughtful assumptions
- validation
- clear limitations
- evidence of judgment

---

### 8. AI Hiring Readability

| Score | Criteria |
|---|---|
| 0 | No structure for automated readers |
| 1 | Keywords without context |
| 2 | Some headings but weak evidence links |
| 3 | Clear headings and skill descriptions |
| 4 | Skill-to-artifact mapping is easy to parse |
| 5 | Machine-readable evidence graph with consistent terminology, links, and claim levels |

Use consistent headings:

- `Business Problem`
- `Target Roles`
- `Skills Demonstrated`
- `Technical Artifacts`
- `Validation Strategy`
- `How to Review This Repo`
- `What This Demonstrates for Hiring Managers`
- `Limitations`
- `Claim Boundary`

---

### 9. Claim Discipline

| Score | Criteria |
|---|---|
| 0 | Exaggerated or misleading claims |
| 1 | Tool name dropping |
| 2 | Mostly safe but vague |
| 3 | Clear lab/simulation language |
| 4 | Safe claims tied to artifacts |
| 5 | Strong claim boundaries with transparent limitations |

Safe claim examples:

- `Snowflake-style SQL patterns`
- `BigQuery-ready SQL examples`
- `DuckDB local simulation`
- `dbt-style analytics engineering lab`
- `Tableau-ready dashboard specification`
- `synthetic ERP/WMS/TMS-style data`
- `AI-assisted workflow with human validation`

Avoid:

- `production deployment`
- `enterprise-grade system`
- `real client implementation`
- `expert-level platform mastery`
- `fully automated production pipeline`

unless fully supported by real evidence.

---

### 10. Portfolio Connectivity

| Score | Criteria |
|---|---|
| 0 | Isolated repo |
| 1 | No link to central roadmap |
| 2 | Basic link only |
| 3 | Links to central roadmap and related repos |
| 4 | Strong cross-linking to evidence map and skill matrix |
| 5 | Fully connected into the portfolio evidence graph |

Each repo should link to:

- central roadmap
- skill coverage matrix
- evidence map
- related repos where useful

---

## Repo Scorecard Template

Use this template during review.

```markdown
# Repo Scorecard

Repository: `<repo-name>`
Review date: `<date>`
Reviewer: `<name or AI review loop>`

| Dimension | Score | Notes | Next Improvement |
|---|---:|---|---|
| Business clarity |  |  |  |
| Technical depth |  |  |  |
| Evidence specificity |  |  |  |
| Validation discipline |  |  |  |
| Role alignment |  |  |  |
| Recruiter readability |  |  |  |
| Hiring manager credibility |  |  |  |
| AI hiring readability |  |  |  |
| Claim discipline |  |  |  |
| Portfolio connectivity |  |  |  |

Average score:
Priority:
Suggested commit message:
Next review angle:
```

---

## Promotion Thresholds

| Average Score | Portfolio Status |
|---:|---|
| 0.0 - 1.9 | Not ready |
| 2.0 - 2.9 | Scaffold only |
| 3.0 - 3.4 | Basic portfolio evidence |
| 3.5 - 3.9 | Needs polish before promotion |
| 4.0 - 4.4 | Strong evidence repo |
| 4.5 - 5.0 | Flagship repo candidate |

A repo should not be pinned or promoted heavily until it reaches at least **4.0**.

---

## Flagship Repo Requirements

A flagship repo should have:

- clear business problem
- strong README
- evidence summary table
- technical artifacts
- validation plan
- role mapping
- limitations
- portfolio context link
- safe claim boundaries
- next improvement backlog

Suggested flagship candidates:

1. `dbt-analytics-engineering-lab`
2. `cloud-warehouse-analytics-lab`
3. `supply-chain-operations-control-tower`
4. `revenue-growth-analytics-engineering`

---

## Anti-Toy Repo Red Flags

A repo may look like a toy project if it has:

- only a README
- generic AI-generated language
- no technical files
- no validation
- no business problem
- no target role
- no data model
- no assumptions
- no limitations
- no repository structure explanation
- files named `test.py`, `demo.sql`, `notes.md`, or `stuff.md`
- tool names without examples
- "production" claims without production evidence

---

## High-Impact Improvement Types

When improving a repo, prefer these changes:

1. Add a concrete technical artifact.
2. Add validation checks.
3. Add an evidence map.
4. Improve the README review path.
5. Add realistic business framing.
6. Add KPI definitions.
7. Add SQL with meaningful transformations.
8. Add dbt models and schema tests.
9. Add Python pipeline checks.
10. Add dashboard specifications.
11. Add CI validation.
12. Add limitations and assumptions.
13. Add cross-links to central roadmap.

Avoid low-impact changes:

- changing emojis
- generic badges
- vague README expansion
- empty directories
- repeated boilerplate
- unrelated files
- unsupported claims

---

## Codex Review Checklist

Before accepting a Codex-generated change, check:

- Did it inspect the repo first?
- Did it implement one focused improvement?
- Did it add or improve a concrete artifact?
- Did it update documentation?
- Did it include validation or quality criteria?
- Did it avoid fake claims?
- Did it keep the repo connected to the portfolio?
- Did it summarize files changed?
- Did it suggest a meaningful next task?

If the change does not improve hiring evidence, reject or revise it.

---

## Final Review Question

Before committing any change, ask:

> Does this make the repo easier for a recruiter, hiring manager, or AI hiring system to understand as credible evidence for a real analytics role?

If the answer is no, the change is not ready.
