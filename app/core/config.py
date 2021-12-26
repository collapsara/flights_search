
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:8000", 
        "https://localhost:8000", 
        "http://localhost", 
        "https://localhost"
    ]

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_URI: Optional[PostgresDsn] = "postgresql://postgres:postgres@database:5432/app"
    

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
