from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import routers
from app.core.config import settings
from database import SessionLocal, engine
from core import models


print(settings.DATABASE_URI)
def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()

app.include_router(routers.provider_a.router, prefix="/provider_a", tags=['provider_a'])
app.include_router(routers.provider_b.router, prefix="/provider_b", tags=['provider_b'])
app.include_router(routers.airflow.router, prefix="/airflow", tags=["airflow"])
app.include_router(routers.rates.router, prefix="", tags=["rates"])

models.Base.metadata.create_all(bind=engine)
