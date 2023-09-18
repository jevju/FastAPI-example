from fastapi import FastAPI

from app.api.api_v1.api import api_router
from app.core.config import settings

from app.api.deps import get_db
from app.db.init_db import init_db

db = get_db()
init_db(db)

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")

app.include_router(api_router, prefix=settings.API_V1_STR)