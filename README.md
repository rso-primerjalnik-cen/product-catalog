# Product catalog microservice

## INFO
Responsible for:
- Fetching product catalog from [nasasuperhrana.si](https://www.nasasuperhrana.si/wp-admin/admin-ajax.php?action=products_data)
- Storing product catalog in database
- Returning a list of all products from the database
- Returning a list of prices for a specific product
- Storing user's favorite products in database
- Updating user's favorite products in database
- Deleting user's favorite products in database

## Build Setup
```bash
# build docker image from Dockerfile
$ docker-compose build

# run docker container in detached mode
$ docker-compose up -d

# get an interactive shell of the running docker-compose service
$ docker-compose exec products_api bash

# stop the container
$ npm run generate
```

## Post config to consul server
```bash
# get an interactive shell of the running docker-compose service
$ docker-compose exec products_api bash
```

```bash
# enter python shell
$ python
```

```python
# import script post_consul_config()
from app.common.scripts import post_consul_config
# run the script
post_consul_config()
```