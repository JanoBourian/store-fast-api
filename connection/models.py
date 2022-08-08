import sqlalchemy
from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, ForeignKey
from .database import database_url

meta = MetaData()

Colors = Table(
    "colors", meta,
    Column("id", String(10), primary_key=True),
    Column("name", String(10), nullable=False)
    )

Sizes = Table("sizes", meta,
    Column("id", String(4), primary_key=True),
    Column("name", String(10), nullable=False)
    )

Users = Table(
    "users", meta,
    Column("id", Integer, primary_key=True),
    Column("email", String(120), unique=True),
    Column("password", String(255), nullable=False),
    Column("full_name", String(200), nullable=False),
    Column("phone", String(13), nullable=False),
    Column("created_at", DateTime, nullable=False, server_default = sqlalchemy.func.now()),
    Column("last_modified_at", DateTime, nullable = False, server_default = sqlalchemy.func.now(), onupdate=sqlalchemy.func.now()),
)

Clothes = Table(
    "clothes", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(120), nullable=False),
    Column("color_id", ForeignKey("colors.id"), nullable=False, index=True),
    Column("size_id", ForeignKey("sizes.id"), nullable=False, index=True),
    Column("photo_url", String(255)),
    Column("created_at", DateTime, nullable=False, server_default = sqlalchemy.func.now()),
    Column("last_modified_at", DateTime, nullable = False, server_default = sqlalchemy.func.now(), onupdate=sqlalchemy.func.now()),
)

engine = sqlalchemy.create_engine(database_url)
meta.create_all(engine)

