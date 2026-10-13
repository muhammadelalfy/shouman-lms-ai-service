# Shouman LMS AI Service

FastAPI service boundary for AI/RAG capabilities, isolated from Laravel business authority. Current scope exposes health and readiness probes while graduation rubric and educational assistant behavior remain gated by OP-1.

## Local verification

```bash
python -m pip install -e '.[dev]'
ruff check .
pytest
```

Deployment is intentionally not configured in this repository yet.
