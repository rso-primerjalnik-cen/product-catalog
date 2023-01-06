from typing import Optional, List
from uuid import uuid4

from pony.orm import db_session
from pony.orm.core import Query, select, desc, QueryResult

from app.common.api.pagination import PaginationParameters
from app.common.models.domain import Product, ProductPrice, ProductFavorites
from app.common.models.rdbms import ProductsPony, ProductPricesPony, ProductFavoritesPony


def order_query(query: Query, order_by: str) -> Query:
    """
    :order_by examples: 'timestamp' order by timestamp ascending,
                        'timestamp__asc' order by timestamp ascending,
                        'timestamp__desc' order by timestamp descending
    """
    try:
        attr, order = order_by.split('__')
        if order == 'desc':
            query = query.order_by(lambda tx: desc(getattr(tx, attr)))
        else:
            query = query.order_by(lambda tx: getattr(tx, attr))
    except ValueError:
        query = query.order_by(lambda tx: getattr(tx, order_by))

    return query


def filter_query(query: Query, **kwargs) -> Query:
    for key, value in kwargs.items():
        try:
            key, operator = key.split('__')
            # Not equal
            if operator == 'neq':
                query = query.filter(lambda entry: getattr(entry, key) != value)
            # Not in
            elif operator == 'nin':
                query = query.filter(lambda entry: getattr(entry, key) not in value)
            # In
            elif operator == 'in':
                query = query.filter(lambda entry: getattr(entry, key) in value)
            # Case Insensitive
            elif operator == 'ci':
                query = query.filter(lambda entry: getattr(entry, key).lower() == value.lower())

        except ValueError:
            query = query.filter(lambda entry: getattr(entry, key) == value)
    return query


# always paginate after filtering since we return results not query
def paginate_query(query: Query, pagination: PaginationParameters) -> QueryResult:
    return QueryResult(query, limit=pagination.limit, offset=pagination.offset, lazy=True)


class PonyProducts(object):
    @db_session
    def get(self, uuid: str) -> Optional[str]:
        product = ProductsPony.get(uuid=uuid)
        return product

    @db_session
    def add(self, model: Product, *args, **kwargs) -> str:
        product = ProductsPony.get(id=model.id)
        if not product:
            # insert happens when we create new pony object in db session
            product = self.to_pony(model)
        return product.uuid

    @db_session
    def list(self, *args, **kwargs) -> List[Product]:
        query: Query = select(fee for fee in ProductsPony)
        pagination = kwargs.pop('pagination', None)

        order_by = kwargs.pop('order_by', None)
        if order_by:
            query = order_query(query, order_by)

        query = filter_query(query, **kwargs)
        if pagination:
            query: QueryResult = paginate_query(query, pagination=pagination)

        return [self.from_pony(fee) for fee in query]

    def to_pony(self, obj: Product) -> ProductsPony:
        return ProductsPony(**obj.dict())

    def from_pony(self, obj: ProductsPony) -> Product:
        return Product(**obj.to_dict())


class PonyProductPrices(object):
    @db_session
    def get(self, uuid: str) -> Optional[str]:
        product = ProductPricesPony.get(uuid=uuid)
        return product

    @db_session
    def add(self, model: ProductPrice, *args, **kwargs) -> str:
        product_price = ProductPricesPony.get(id=model.id)
        if not product_price:
            # insert happens when we create new pony object in db session
            product_price = self.to_pony(model)
        return product_price.uuid

    @db_session
    def list(self, *args, **kwargs) -> List[ProductPrice]:
        query: Query = select(fee for fee in ProductPricesPony)
        pagination = kwargs.pop('pagination', None)

        order_by = kwargs.pop('order_by', None)
        if order_by:
            query = order_query(query, order_by)

        query = filter_query(query, **kwargs)
        if pagination:
            query: QueryResult = paginate_query(query, pagination=pagination)

        return [self.from_pony(fee) for fee in query]

    def to_pony(self, obj: ProductPrice) -> ProductPricesPony:
        return ProductPricesPony(**obj.dict())

    def from_pony(self, obj: ProductPricesPony) -> ProductPrice:
        return ProductPrice(**obj.to_dict())


class PonyProductFavorites(object):
    @db_session
    def get(self, user_uuid: str) -> ProductFavorites:
        product = ProductFavoritesPony.get(user_uuid=user_uuid)
        return self.from_pony(product) if product else None

    @db_session
    def add(self, model: ProductFavorites, *args, **kwargs) -> str:
        product_favorite = ProductFavoritesPony.get(user_uuid=model.user_uuid)
        if not product_favorite:
            # insert happens when we create new pony object in db session
            product_favorite = self.to_pony(model)
        return product_favorite.uuid

    @db_session
    def update(self, uuid: str, model: ProductFavorites, *args, **kwargs) -> ProductFavorites:
        model_dict = model.dict()
        model_dict.pop('uuid', None)
        product_list = model_dict.pop('product_uuids', [])

        if not product_list:
            products_string = None
        else:
            products_string = ','.join(product_list)

        ProductFavoritesPony[uuid].set(product_uuids=products_string, **model_dict)
        return model

    def to_pony(self, obj: ProductFavorites) -> ProductFavoritesPony:
        o = obj.dict()
        product_list = o.pop('product_uuids', [])
        uuid = o.pop('uuid', None)

        if not uuid:
            uuid = str(uuid4())

        if not product_list:
            products_string = None
        else:
            products_string = ','.join(product_list)

        return ProductFavoritesPony(uuid=uuid, product_uuids=products_string, **o)

    def from_pony(self, obj: ProductFavoritesPony) -> ProductFavorites:
        o = obj.to_dict()
        product_list = o.pop('product_uuids', None)

        if not product_list:
            products = []
        else:
            products = product_list.split(',')
        return ProductFavorites(product_uuids=products, **o)
