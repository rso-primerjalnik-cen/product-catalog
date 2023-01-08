from consul import Consul


class Settings(object):
    POSTGRESQL_HOST = None
    POSTGRESQL_PWD = None
    POSTGRESQL_USER = None
    POSTGRESQL_DB = None
    PAGINATION_DEFAULT_LIMIT: int = 20
    PAGINATION_DEFAULT_OFFSET: int = 0
    CONSUL_HOST = 'my-consul'
    PRODUCTS_LIVENESS_CHECK = 'good'
    FAULT_TOLERANCE_CHECK = 'good'
    c = None

    def __init__(self):
        import os
        from dotenv import load_dotenv
        load_dotenv()
        consul_host = os.getenv('CONSUL_HOST')
        self.CONSUL_HOST = consul_host if consul_host else self.CONSUL_HOST
        self.c = Consul(host=self.CONSUL_HOST)

    @property
    def postgres_conn(self):
        return dict(provider="postgres",
                    host=self.get_postgresql_host(),
                    password=self.get_postgresql_pwd(),
                    user=self.get_postgresql_user(),
                    database=self.get_postgresql_db())

    def get_fault_tolerance_check(self):
        index = None
        index, data = self.c.kv.get('FAULT_TOLERANCE_CHECK', index=index)
        if data is not None:
            self.FAULT_TOLERANCE_CHECK = data['Value'].decode("utf-8")
        return self.FAULT_TOLERANCE_CHECK

    def get_liveness_check(self):
        index = None
        index, data = self.c.kv.get('PRODUCTS_LIVENESS_CHECK', index=index)
        if data is not None:
            self.PRODUCTS_LIVENESS_CHECK = data['Value'].decode("utf-8")
        return self.PRODUCTS_LIVENESS_CHECK

    def get_postgresql_host(self):
        index = None
        index, data = self.c.kv.get('POSTGRESQL_HOST', index=index)
        if data is not None:
            self.POSTGRESQL_HOST = data['Value'].decode("utf-8")
        return self.POSTGRESQL_HOST

    def get_postgresql_pwd(self):
        index = None
        index, data = self.c.kv.get('POSTGRESQL_PWD', index=index)
        if data is not None:
            self.POSTGRESQL_PWD = data['Value'].decode("utf-8")
        return self.POSTGRESQL_PWD

    def get_postgresql_user(self):
        index = None
        index, data = self.c.kv.get('POSTGRESQL_USER', index=index)
        if data is not None:
            self.POSTGRESQL_USER = data['Value'].decode("utf-8")
        return self.POSTGRESQL_USER

    def get_postgresql_db(self):
        index = None
        index, data = self.c.kv.get('POSTGRESQL_DB', index=index)
        if data is not None:
            self.POSTGRESQL_DB = data['Value'].decode("utf-8")
        return self.POSTGRESQL_DB


def get_settings() -> Settings:
    return Settings()

# async def watch_consul():
#     c = consul.aio.Consul(host='my-consul')
#     index = None
#     while True:
#         try:
#             index, data = await c.kv.get('POSTGRESQL_HOST', index=index)
#             print('***********************************', data)
#             if data is not None:
#                 config.POSTGRESQL_HOST = data['Value']
#
#             index, data = await c.kv.get('POSTGRESQL_PWD', index=index)
#             if data is not None:
#                 config.POSTGRESQL_PWD = data['Value']
#
#             index, data = await c.kv.get('POSTGRESQL_USER', index=index)
#             if data is not None:
#                 config.POSTGRESQL_USER = data['Value']
#
#             index, data = await c.kv.get('POSTGRESQL_DB', index=index)
#             if data is not None:
#                 config.POSTGRESQL_DB = data['Value']
#
#         except consul.base.Timeout as e:
#             # gracefully handle request timeout
#             print('Consul Timeoutttttttttttt', e)
