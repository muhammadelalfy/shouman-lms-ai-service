"""LMS AI Service entry point.

Owns (per CLAUDE.md §73): retrieval, embeddings, RAG, prompt orchestration,
model routing, AI tools. Laravel owns authentication, authorization, quotas,
business rules, and usage/billing.

Current scope: health endpoints only. Rubric-based graduation-project
evaluation (FR-PRJ-3) and the educational assistant are blocked on OP-1
(approved Rubric) — see docs/requirements/srs.md §10.
"""

from fastapi import FastAPI

app = FastAPI(title="LMS AI Service", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    """Liveness probe."""
    return {"status": "alive"}


@app.get("/ready")
def ready() -> dict[str, str]:
    """Readiness probe. Will check pgvector/LLM provider reachability once wired."""
    return {"status": "ready"}
