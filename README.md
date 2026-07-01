# AI-Native Analytics Portfolio Roadmap

This repository is the source of truth for a coverage-driven analytics portfolio. The portfolio is organized to demonstrate modern Data & Analytics Engineering, Business Intelligence, Analytics Engineering, Data Pipelines, Supply Chain Analytics, Revenue/Growth Analytics, and AI-Augmented Data Workflows.

## Positioning Statement

My GitHub portfolio is organized as a coverage-driven evidence system for modern Data & Analytics Engineering roles, demonstrating SQL, Python, BI, dbt, cloud warehouse concepts, orchestration, data quality, CI/CD, supply chain analytics, revenue analytics, and AI-native analytical execution.

## Approved New Repositories

| Repository | Purpose |
|---|---|
| `AI-Native-Analytics-Portfolio-Roadmap` | Central control plane for portfolio strategy, standards, evidence mapping, claim boundaries and review workflow. |
| `cloud-warehouse-analytics-lab` | Demonstrate Snowflake, BigQuery, Redshift, Synapse, Databricks concepts and local DuckDB warehouse simulation. |
| `dbt-analytics-engineering-lab` | Demonstrate dbt-style staging, intermediate, marts, tests, documentation, lineage and BI-ready models. |
| `orchestration-data-pipelines-lab` | Demonstrate Airflow, Prefect, Dagster, Azure Data Factory, SSIS concepts, logging, retries and error handling. |
| `tableau-bi-dashboard-lab` | Demonstrate Tableau, Looker, Sigma, dashboard specifications, calculated fields and semantic-layer thinking. |
| `supply-chain-operations-control-tower` | Demonstrate ERP/WMS/TMS-style operations analytics and supply chain KPI control tower design. |
| `revenue-growth-analytics-engineering` | Demonstrate funnel, cohort, retention, churn, segmentation and revenue analytics. |

## Current Evidence Ledger

The current source of truth for skill-to-artifact mapping is:

- `PORTFOLIO_EVIDENCE_LEDGER.csv`
- `tools/validate_evidence_ledger.py`

Run:

```bash
python tools/validate_evidence_ledger.py
```

The ledger maps each major skill cluster to a repository, concrete artifacts, validation method, claim level, target roles, PR/review status and next improvement.

## Guardrails

- Labs are simulations, examples, patterns or local implementations unless explicitly proven otherwise.
- Avoid fake production, client, employer or enterprise deployment claims.
- Every artifact should be useful, inspectable, and mapped to a job skill.
- AI-assisted generation is acceptable only with human review, validation notes and clear limitations.

## Publishing Workflow

1. Build complete repo-ready packages locally.
2. Review files, run lightweight validation and check claims.
3. Upload each package to GitHub manually as a ZIP, through GitHub Desktop, or via CLI.
4. Use future hourly automation for polish, validation, README improvements and targeted commit suggestions.
