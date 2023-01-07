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
