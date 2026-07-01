"""Validate the portfolio evidence ledger.

This script keeps the central roadmap honest: every portfolio claim must map to
an approved repository, a specific artifact path, a validation method, target
roles, and a safe claim level.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER_PATH = ROOT / "PORTFOLIO_EVIDENCE_LEDGER.csv"

REQUIRED_COLUMNS = {
    "skill_cluster",
    "evidence_repository",
    "artifact_path",
    "what_it_proves",
    "validation_method",
    "claim_level",
    "target_roles",
    "status",
    "pr_url",
    "next_improvement",
}

APPROVED_REPOSITORIES = {
    "AI-Native-Analytics-Portfolio-Roadmap",
    "cloud-warehouse-analytics-lab",
    "dbt-analytics-engineering-lab",
    "orchestration-data-pipelines-lab",
    "tableau-bi-dashboard-lab",
    "supply-chain-operations-control-tower",
    "revenue-growth-analytics-engineering",
}

CLAIM_LEVELS = {
    "Strong evidence",
    "Lab evidence",
    "Pattern evidence",
    "Planned evidence",
    "Weak evidence",
}

STATUSES = {
    "Draft PR opened",
    "In review",
    "Merged",
    "Planned",
}


class LedgerValidationError(Exception):
    """Raised when the evidence ledger fails deterministic checks."""


def read_ledger() -> list[dict[str, str]]:
    with LEDGER_PATH.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def validate_ledger(rows: list[dict[str, str]]) -> dict[str, object]:
    if not rows:
        raise LedgerValidationError("Evidence ledger has no rows")

    missing_columns = REQUIRED_COLUMNS - set(rows[0])
    if missing_columns:
        raise LedgerValidationError(f"Missing required columns: {sorted(missing_columns)}")

    errors: list[str] = []
    repo_counts = {repo: 0 for repo in APPROVED_REPOSITORIES}
    seen_keys: set[tuple[str, str, str]] = set()

    for line_number, row in enumerate(rows, start=2):
        for column in REQUIRED_COLUMNS - {"pr_url"}:
            if not row[column].strip():
                errors.append(f"line {line_number}: {column} is required")

        repo = row["evidence_repository"]
        if repo not in APPROVED_REPOSITORIES:
            errors.append(f"line {line_number}: unapproved repository {repo}")
        else:
            repo_counts[repo] += 1

        if row["claim_level"] not in CLAIM_LEVELS:
            errors.append(f"line {line_number}: invalid claim level {row['claim_level']}")

        if row["status"] not in STATUSES:
            errors.append(f"line {line_number}: invalid status {row['status']}")

        if row["status"] == "Draft PR opened" and not row["pr_url"].startswith("https://github.com/net421/"):
            errors.append(f"line {line_number}: draft PR rows need a net421 GitHub PR URL")

        key = (row["skill_cluster"], repo, row["artifact_path"])
        if key in seen_keys:
            errors.append(f"line {line_number}: duplicate skill/repo/artifact key")
        seen_keys.add(key)

    missing_repos = [repo for repo, count in sorted(repo_counts.items()) if count == 0]
    if missing_repos:
        errors.append(f"missing approved repositories: {', '.join(missing_repos)}")

    if errors:
        raise LedgerValidationError("; ".join(errors))

    return {
        "rows": len(rows),
        "approved_repositories_covered": len([repo for repo, count in repo_counts.items() if count > 0]),
        "draft_pr_rows": sum(1 for row in rows if row["status"] == "Draft PR opened"),
        "strong_evidence_rows": sum(1 for row in rows if row["claim_level"] == "Strong evidence"),
        "lab_evidence_rows": sum(1 for row in rows if row["claim_level"] == "Lab evidence"),
        "pattern_evidence_rows": sum(1 for row in rows if row["claim_level"] == "Pattern evidence"),
    }


def main() -> None:
    summary = validate_ledger(read_ledger())
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
