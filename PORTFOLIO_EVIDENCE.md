# Portfolio Evidence Index

The machine-readable source of truth is `PORTFOLIO_RELEASE_LEDGER.json`; the flat review view is `PORTFOLIO_EVIDENCE_LEDGER.csv`.

| Evidence area | Primary repository | Validation signal | Claim boundary |
|---|---|---|---|
| Supply-chain operations | `supply-chain-operations-control-tower` | KPI/data checks and tests | Synthetic operational data |
| Cloud warehouse | `cloud-warehouse-analytics-lab` | DB/export reconciliation and reproducibility | Local DuckDB plus platform patterns |
| Analytics engineering | `dbt-analytics-engineering-lab` | 101 successful dbt results | Local deterministic project |
| Orchestration/DataOps | `orchestration-data-pipelines-lab` | Failure/recovery, idempotency and tests | Framework mappings are not hosted deployments |
| BI engineering | `tableau-bi-dashboard-lab` | Cross-extract metric reconciliation | No proprietary workbook deployment claim |
| Revenue/growth | `revenue-growth-analytics-engineering` | SQL and governance reconciliation | Observational synthetic analysis |
| Semantic AI agent | `semantic-layer-ai-agent-lab` | Grounding, lineage, refusals and upstream drift checks | Governed question set and read-only SQL |
| MLOps/LLMOps | `mlops-llmops-evaluation-lab` | Model gates plus shared agent release gate | Local deterministic evaluation system |
| Decision twin | `supply-chain-decision-twin-agent` | Dify compatibility, scenarios, ranking and no-autonomy checks | Human-reviewed support only |
| Causal experimentation | `causal-experimentation-lab` | Scientific reproduction and 24-check release envelope | Synthetic randomized demonstration |
| Cloud execution | `cloud-executable-analytics-lab` | Container execution with read-only root filesystem | Fargate target design, not active deployment |

A claim is promoted only when it resolves to a repository, artifact, validation signal and explicit limitation.
