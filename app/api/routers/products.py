from uuid import uuid4

import requests
from fastapi import APIRouter

from app.api.serializers.products import ProductFavoritesIn
from app.common.models.domain import Product, ProductPrice, ProductFavorites
from app.common.models.rdbms import ProductPricesPony
from app.common.repository.rdbms import PonyProducts, PonyProductPrices, PonyProductFavorites

router = APIRouter(prefix='/products', tags=['Products'])


@router.get('/')
async def get_all_products_api():
    r = requests.get('https://www.nasasuperhrana.si/wp-admin/admin-ajax.php?action=products_data')
    product_repo = PonyProducts()
    price_repo = PonyProductPrices()

    for p in r.json().get('products'):
        product_prices = p.pop('prices', [])
        new_product = Product(uuid=str(uuid4()), **p)
        product_repo.add(new_product)

        new_product_prices = [ProductPrice(uuid=str(uuid4()), **pp) for pp in product_prices]

        for pp in new_product_prices:
            pp.product = new_product.uuid
            price_repo.add(pp)

    return 'Success'


@router.get('/db/')
async def get_all_products_db():
    repo = PonyProducts()
    return repo.list()


@router.get('/{product_uuid}/prices/')
async def get_product_prices_from_db(product_uuid: str):
    repo = PonyProductPrices()
    return repo.list(product=product_uuid)


@router.post('/favorites/{user_uuid}/')
async def add_users_favorite_products(user_uuid: str, products: ProductFavoritesIn):
    repo = PonyProductFavorites()

    favs: ProductFavorites = repo.get(user_uuid=user_uuid)

    if not favs:
        repo.add(ProductFavorites(user_uuid=user_uuid, product_uuids=products.product_uuids))
    else:
        repo.update(uuid=favs.uuid, model=ProductFavorites(user_uuid=user_uuid, product_uuids=products.product_uuids))

    return repo.get(user_uuid=user_uuid)


@router.get('/favorites/{user_uuid}/')
async def get_users_favorite_products(user_uuid: str):
    repo = PonyProductFavorites()
    favs = repo.get(user_uuid=user_uuid)

    if not favs:
        repo.add(ProductFavorites(user_uuid=user_uuid, products=[]))
        return repo.get(user_uuid=user_uuid)
    return favs
