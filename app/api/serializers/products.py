from typing import Optional, List

from pydantic import BaseModel


class ProductFavoritesIn(BaseModel):
    product_uuids: List[str]
