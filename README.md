# LMS AI Service

Python FastAPI service for AI/RAG workloads, isolated from the Laravel monolith per [CLAUDE.md §73](../CLAUDE.md).

**Status: skeleton.** Implementation starts once the graduation-project Rubric is approved (OP-1, [SRS §10](../docs/requirements/srs.md)).

## Responsibilities
- Rubric-based graduation-project analysis (advisory only — human evaluators decide)
- Embeddings + RAG over course content (PostgreSQL + pgvector)
- Prompt orchestration and model routing

## Run (requires Python 3.12+)

```bash
pip install -e .[dev]
uvicorn app.main:app --reload --port 8001
```
