# Portfolio Evidence Index

The validated, current artifact-level evidence map lives in `PORTFOLIO_EVIDENCE_LEDGER.csv`.

Run the ledger validator:

```bash
python tools/validate_evidence_ledger.py
```

The table below is a high-level planning index. The ledger is the source of truth for current skill clusters, artifacts, validation methods, claim levels and PR status.

| Evidence Area | Current Package | Next Improvement |
|---|---|---|
| Cloud warehouse concepts | `cloud-warehouse-analytics-lab` | Add cost/performance notes and platform-specific query review checklist. |
| dbt analytics engineering | `dbt-analytics-engineering-lab` | Add dbt adapter profile or CI parse/test workflow. |
| Orchestration | `orchestration-data-pipelines-lab` | Add Dagster asset example and GitHub Actions validation workflow. |
| BI dashboard specification | `tableau-bi-dashboard-lab` | Add sample dashboard screenshot/mock or workbook build checklist. |
| Supply chain control tower | `supply-chain-operations-control-tower` | Add sample validation output file and dashboard mock export. |
| Revenue growth analytics | `revenue-growth-analytics-engineering` | Add retention visualization output or dashboard-ready extract. |
| AI-native portfolio governance | `AI-Native-Analytics-Portfolio-Roadmap` | Add recruiter guide and job target map. |
