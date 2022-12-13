from typing import Optional

from ..settings import get_settings
from pydantic import BaseModel
from fastapi import Request


settings = get_settings()


class PaginationParameters(BaseModel):
    limit: int = settings.PAGINATION_DEFAULT_LIMIT
    offset: int = settings.PAGINATION_DEFAULT_OFFSET


async def pagination_parameters(limit: int = settings.PAGINATION_DEFAULT_LIMIT,
                                offset: int = settings.PAGINATION_DEFAULT_OFFSET) -> PaginationParameters:
    return PaginationParameters(limit=limit,
                                offset=offset)


def get_pagination_next(request: Request, total_count: Optional[int] = None) -> Optional[str]:
    limit = int(request.query_params.get("limit") or get_settings().PAGINATION_DEFAULT_LIMIT)
    offset = int(request.query_params.get("offset") or get_settings().PAGINATION_DEFAULT_OFFSET) + limit
    if total_count and offset >= total_count:
        return None
    return f'{str(request.base_url)[:-1]}{request.scope.get("path")}?limit={limit}&offset={offset}'


def get_pagination_previous(request: Request) -> Optional[str]:
    limit = int(request.query_params.get("limit") or get_settings().PAGINATION_DEFAULT_LIMIT)
    offset = int(request.query_params.get("offset") or get_settings().PAGINATION_DEFAULT_OFFSET) - limit
    if offset <= -limit:
        return None
    if offset < 0:
        offset = 0
    return f'{str(request.base_url)[:-1]}{request.scope.get("path")}?limit={limit}&offset={offset}'
