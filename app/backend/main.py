"""Aplicacao FastAPI do IPIT Learning Engine."""

from fastapi import FastAPI

from app.backend.api.health import router as health_router
from app.backend.config import get_settings


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=(
        "Backend do Learning Engine do IPIT — Ideathon Pedagogico de "
        "Inovacao Tecnologica, de autoria metodologica de Sandra Maria Pereira."
    ),
)
app.include_router(health_router)
