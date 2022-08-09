import sqlalchemy
from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Boolean,
)
from .database import database_url

meta = MetaData()

Colors = Table(
    "colors",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(10), nullable=False, unique=True),
    Column("description", String(255)),
)

Sizes = Table(
    "sizes",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(10), nullable=False, unique=True),
    Column("description", String(255)),
)

Roles = Table(
    "roles",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(20), nullable=False, unique=True),
    Column("description", String(255)),
    Column("active", Boolean(True), nullable=False),
)

Users = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True),
    Column("email", String(120), unique=True),
    Column("password", String(255), nullable=False),
    Column("full_name", String(200), nullable=False, unique=True),
    Column("phone", String(13), nullable=False, unique=True),
    Column(
        "created_at", DateTime, nullable=False, server_default=sqlalchemy.func.now()
    ),
    Column(
        "last_modified_at",
        DateTime,
        nullable=False,
        server_default=sqlalchemy.func.now(),
        onupdate=sqlalchemy.func.now(),
    ),
    Column(
        "role_id",
        ForeignKey("roles.id"),
        nullable=False
    ),
)

Clothes = Table(
    "clothes",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(120), nullable=False),
    Column("color_id", ForeignKey("colors.id"), nullable=False, index=True),
    Column("size_id", ForeignKey("sizes.id"), nullable=False, index=True),
    Column("photo_url", String(255)),
    Column(
        "created_at", DateTime, nullable=False, server_default=sqlalchemy.func.now()
    ),
    Column(
        "last_modified_at",
        DateTime,
        nullable=False,
        server_default=sqlalchemy.func.now(),
        onupdate=sqlalchemy.func.now(),
    ),
)

engine = sqlalchemy.create_engine(database_url)
meta.create_all(engine)
