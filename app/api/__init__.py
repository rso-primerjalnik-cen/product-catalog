from fastapi import FastAPI, APIRouter

from app.api.routers import products
from app.common.models.rdbms import db
from app.common.settings import get_settings

API_PREFIX = '/api/v1'

fastapi_app = FastAPI(docs_url=f"{API_PREFIX}/products/docs")

settings = get_settings()

r = APIRouter()


@r.get('/health/')
async def entrypoint():
    return dict(status='OK')

fastapi_app.include_router(products.router, prefix=API_PREFIX)
fastapi_app.include_router(r)


@fastapi_app.on_event("startup")
async def startup():
    # Pony ORM
    db.bind(**settings.postgres_conn)
    db.generate_mapping(create_tables=False, check_tables=True)
