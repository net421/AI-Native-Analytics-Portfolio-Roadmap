# Integration Architecture

## Integration classes

### Strict, commit-pinned integrations

1. `semantic-layer-ai-agent-lab` validates real SQL contracts from:
   - `dbt-analytics-engineering-lab@263134172e4ec3f422b47c25d01a86555ea29df9`
   - `cloud-warehouse-analytics-lab@140b076edcb89c3b27c3786887ee17d21494a44d`
2. `mlops-llmops-evaluation-lab` executes and normalizes evidence from:
   - `semantic-layer-ai-agent-lab@23297a682a17bc9e89a31f37bf9f67defbeadc98`
   - `supply-chain-decision-twin-agent@28fd0986ccadec740dd9ab9e67cbd955885f0d64`
   - the pinned dbt and warehouse releases above.

These are the only cross-repository relationships represented as runtime or CI release dependencies.

## Conceptual portfolio relationships

The foundational repositories are intentionally executable in isolation. The orchestration, BI, supply-chain and revenue projects demonstrate compatible layers and practices, but the Roadmap does not claim they are deployed as one monolith.

- The orchestration lab demonstrates validation-first movement and publication patterns.
- The BI lab demonstrates governed consumption and metric reconciliation.
- The supply-chain and revenue projects provide domain analytical evidence.
- The causal lab provides experiment and review governance independent of agent execution.
- The cloud-executable lab provides a container/runtime pattern independent of a real AWS deployment.
- The Decision Twin preserves a real Dify/FastAPI integration while keeping operational execution disabled.

## Responsibility boundaries

| Component | Responsible for | Explicitly not responsible for |
|---|---|---|
| Warehouse/dbt | governed transformations and analytical relations | autonomous decisions |
| Semantic Agent | safe question planning and grounded read-only answers | unrestricted SQL or operational writes |
| Decision Twin | deterministic scenario support and ranked recommendations | purchase orders, transfers or supplier commitments |
| Shared evaluator | release evidence and fail-closed checks | continuous hosted monitoring |
| Causal lab | synthetic randomized evidence and review envelope | real-world treatment-effect claims |
| Cloud executable lab | reproducible container execution | proof of an active AWS deployment |
