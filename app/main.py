"""LMS AI service entry point."""
from fastapi import FastAPI

app = FastAPI(title="Shouman LMS AI Service", version="0.1.0")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "alive"}

@app.get("/ready")
def ready() -> dict[str, str]:
    return {"status": "ready"}
