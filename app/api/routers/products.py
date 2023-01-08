from uuid import uuid4

import requests
from circuitbreaker import circuit, CircuitBreakerMonitor
from fastapi import APIRouter, HTTPException
from starlette import status
from starlette.responses import Response

from app.api.serializers.products import ProductFavoritesIn
from app.common.models.domain import Product, ProductPrice, ProductFavorites
from app.common.repository.rdbms import PonyProducts, PonyProductPrices, PonyProductFavorites
from app.common.settings import get_settings

router = APIRouter(prefix='/products', tags=['Products'])

FAILURES = 3
TIMEOUT = 30


def fallback(*args, **kwargs):
    print('CIRCUIT BREAKER OPENED AND FALLBACK FUNCTION CALLED')
    for x in CircuitBreakerMonitor.get_circuits():
        print(f'Circuit name: {x.name}')
        print(f'Circuit state: {x.name}')
        print(f'Circuit will be open until {x.open_remaining} seconds pass')
    return None


@circuit(failure_threshold=FAILURES, recovery_timeout=TIMEOUT,
         fallback_function=fallback, expected_exception=HTTPException)
def call_bad_url():
    s = get_settings()
    fault_tolerance_check = s.get_fault_tolerance_check()
    if fault_tolerance_check == 'bad':
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail='Fault tolerance endpoint raised an exception')
    return dict(status='OK')


@router.get('/fault-tolerance/')
async def fault_tolerance_example():
    return call_bad_url()


@router.get('/health/live/')
async def health_check_liveness():
    s = get_settings()
    liveness_check = s.get_liveness_check()
    if liveness_check == 'bad':
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail='Liveness check failed')
    return dict(status='OK')


@router.get('/health/ready/')
async def health_check_readiness():
    repo = PonyProducts()
    try:
        repo.list()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(e))
    return dict(status='OK')


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
async def get_users_favorite_products(user_uuid: str, just_uuid: int = 1):
    repo = PonyProductFavorites()
    favs = repo.get(user_uuid=user_uuid)

    if not favs:
        repo.add(ProductFavorites(user_uuid=user_uuid, products=[]))
        favs = repo.get(user_uuid=user_uuid)

    if not just_uuid:
        product_repo = PonyProducts()
        favs.products = product_repo.list(uuid__in=favs.product_uuids)
    return favs


@router.delete('/favorites/{user_uuid}/{product_uuid}/')
async def delete_users_favorite_product(user_uuid: str, product_uuid: str):
    return Response(status_code=status.HTTP_204_NO_CONTENT, content='Deleted successfully')
