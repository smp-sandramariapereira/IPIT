"""Configuracao central do backend IPIT via variaveis de ambiente."""

from dataclasses import dataclass
from functools import lru_cache
import os


@dataclass(frozen=True, slots=True)
class Settings:
    """Configuracoes imutaveis da aplicacao."""

    app_name: str = "IPIT Learning Engine"
    app_version: str = "0.1.0"
    app_environment: str = "development"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Carrega e memoriza configuracoes do processo atual."""

    return Settings(
        app_name=os.getenv("APP_NAME", "IPIT Learning Engine"),
        app_version=os.getenv("APP_VERSION", "0.1.0"),
        app_environment=os.getenv("APP_ENVIRONMENT", "development"),
    )
