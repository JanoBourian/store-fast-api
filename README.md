# store-fast-api
A store development with fastapi

# Create a docker container with the postgresql database

## Steps for create and run the PostgreSQL container

Steps
```bash
* Download the official image
* Check the image
* Run the container with the next flags:
    * --name: container name
    * --env/-e: environment variables
    * -p: port assigment (<local>:<external>)
    * -v: where the data will be saved
    * --detach/-d: if you prefer execute it in background
* Try the connection and availability
```

Commands
```bash
docker ps
docker ps -a
docker pull postgres:latest
docker images

docker run \ 
    --name fastapi-postgres \
    -e POSTGRES_PASSWORD=mysecretpassword \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
    -v C:<path>\aws-fastapi:/var/lib/postgresql/data \
    -p 5432:5432 \
    -d postgres:latest
    
docker logs fastapi-postgres
docker exec -it fastapi-postgres bash
```

If you want to start the postgres console

```bash
docker ps
docker exec -it CONTAINER_ID bash
psql -h localhost -p 5432 -U postgres -W
\l 
\c postgres
\d
\dt
```

# Alembic

Alembic is our migration manager

In alembic.ini 

```ini
sqlalchemy.url 
```

In migrations/env.py
```python
from connection.models import meta
target_metadata = meta
```

```bash
alembic init migrations
# Delete or change information
alembic revision --autogenerate -m "Initial"
alembic upgrade head
# Delete or change information into models file
alembic revision --autogenerate -m "Delete Test table"
alembic upgrade head
```