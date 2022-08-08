import databases
from config.config import env

def get_database_url() -> str:
    ## Local vars
    drivername = "postgresql"
    db_user = env("DB_USER")
    db_pass = env("DB_PASSWORD")
    db_name = env("DB_NAME")
    db_host = env("INSTANCE_HOST")
    db_port = env("DB_PORT")
    connection = (
        drivername
        + "://"
        + db_user
        + ":"
        + db_pass
        + "@"
        + db_host
        + ":"
        + db_port
        + "/"
        + db_name
    )
    return connection

database_url = get_database_url()
database = databases.Database(database_url)    