import consul


def post_consul_config():
    import os
    from dotenv import load_dotenv
    load_dotenv()
    c = consul.Consul(host=os.getenv('CONSUL_HOST'))
    c.kv.put('POSTGRESQL_HOST', os.getenv('POSTGRESQL_HOST'))
    c.kv.put('POSTGRESQL_PWD', os.getenv('POSTGRESQL_PWD'))
    c.kv.put('POSTGRESQL_USER', os.getenv('POSTGRESQL_USER'))
    c.kv.put('POSTGRESQL_DB', os.getenv('POSTGRESQL_DB'))
    c.kv.put('PRODUCTS_LIVENESS_CHECK', os.getenv('PRODUCTS_LIVENESS_CHECK'))
    c.kv.put('FAULT_TOLERANCE_CHECK', os.getenv('FAULT_TOLERANCE_CHECK'))
