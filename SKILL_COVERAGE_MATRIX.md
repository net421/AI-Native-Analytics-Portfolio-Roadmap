# Skill Coverage Matrix

This matrix is the human-readable skill map. The current artifact-level source of truth is `PORTFOLIO_EVIDENCE_LEDGER.csv`, validated by `tools/validate_evidence_ledger.py`.

| Skill | Evidence repo | Artifact | Status | Claim Level |
|---|---|---|---|---|
| Advanced SQL | `dbt-analytics-engineering-lab` / `cloud-warehouse-analytics-lab` | CTEs, joins, windows, marts, validation queries | Draft PRs opened | Lab evidence |
| Python analytics | multiple labs | validation scripts, KPI calculators, local simulators | Draft PRs opened | Lab evidence |
| dbt | `dbt-analytics-engineering-lab` | staging, intermediate, marts, schema tests, singular tests | Draft PR opened | Lab evidence |
| Snowflake | `cloud-warehouse-analytics-lab` | `snowflake/sql/analytics_mart_patterns.sql` | Draft PR opened | Lab evidence |
| BigQuery | `cloud-warehouse-analytics-lab` | `bigquery/sql/order_mart_pattern.sql` | Draft PR opened | Lab evidence |
| Databricks | `cloud-warehouse-analytics-lab` | PySpark equivalents and lakehouse notes | Base artifact exists | Pattern evidence |
| Redshift / Synapse | `cloud-warehouse-analytics-lab` | comparison docs and SQL patterns | Base artifact exists | Pattern evidence |
| Tableau | `tableau-bi-dashboard-lab` | calculated fields, dashboard spec, data contract validator | Draft PR opened | Lab evidence |
| Looker / Sigma | `tableau-bi-dashboard-lab` | semantic layer concepts, LookML-style examples, Sigma guardrails | Draft PR opened | Pattern evidence |
| Airflow / ADF | `orchestration-data-pipelines-lab` | Airflow DAG, ADF mapping, validation-first simulator | Draft PR opened | Pattern evidence |
| Prefect / Dagster | `orchestration-data-pipelines-lab` | Prefect flow and Dagster mapping | Draft PR opened; Dagster example still needed | Pattern evidence |
| SSIS concepts | `orchestration-data-pipelines-lab` | enterprise ETL concept mapping | Draft PR opened | Pattern evidence |
| Data Quality | all labs | dbt tests, SQL checks, Python validators, dashboard data contract | Draft PRs opened | Lab evidence |
| Supply Chain KPIs | `supply-chain-operations-control-tower` | OTIF, fill rate, inventory, lead time, freight cost | Draft PR opened | Lab evidence |
| Revenue / Growth | `revenue-growth-analytics-engineering` | funnel, cohort, retention, churn, segmentation | Draft PR opened | Lab evidence |
| Stakeholder storytelling | all repos | summaries, dashboard specs, review guides, assumptions | Draft PRs opened | Lab evidence |
| AI-native workflow | roadmap + all repos | human validation, evidence ledger, safe claim boundaries | In review | Strong evidence |
