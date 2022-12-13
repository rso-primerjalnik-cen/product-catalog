from uuid import uuid4

import requests
from fastapi import APIRouter

from app.common.models.domain import Product, ProductPrice
from app.common.models.rdbms import ProductPricesPony
from app.common.repository.rdbms import PonyProducts, PonyProductPrices

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
async def get_all_products():
    repo = PonyProducts()
    return repo.list()
