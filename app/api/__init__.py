from fastapi import FastAPI

from app.api.routers import products
from app.common.settings import get_settings

fastapi_app = FastAPI()

settings = get_settings()

API_PREFIX = '/api/v1'
fastapi_app.include_router(products.router, prefix=API_PREFIX)
