"""Endpoint de verificacao de saude do backend IPIT."""

from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel

from app.backend.config import get_settings


router = APIRouter(tags=["operacao"])


class HealthResponse(BaseModel):
    """Contrato publico do health check."""

    status: Literal["ok"]
    service: str
    version: str
    environment: str


@router.get("/health", response_model=HealthResponse, summary="Verificar saude da API")
def health_check() -> HealthResponse:
    """Confirma que o processo da API esta disponivel."""

    settings = get_settings()
    return HealthResponse(
        status="ok",
        service=settings.app_name,
        version=settings.app_version,
        environment=settings.app_environment,
    )
