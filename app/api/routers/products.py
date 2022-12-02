import requests
from fastapi import APIRouter

router = APIRouter(prefix='/products', tags=['Products'])


@router.get('/')
async def get_all_products():
    r = requests.get('https://www.nasasuperhrana.si/wp-admin/admin-ajax.php?action=products_data')
    return r.json()
