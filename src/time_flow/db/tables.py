"""Tables DataBase."""

from sqlalchemy import (
    Column,
    DateTime,
    String,
    Table,
    text,
)
from sqlalchemy.dialects.postgresql import UUID

from .base import metadata

tasks = Table(
    "tasks",
    metadata,
    Column(
        "uid",
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    ),
    Column("title", String(255), nullable=False),
    Column(
        "created_at",
        DateTime(timezone=True),
        server_default=text("now()"),
        nullable=False,
    ),
)

user = Table(
    "user",
    metadata,
    Column(
        "uid",
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    ),
    Column("name", String(255), nullable=False),
    Column(
        "created_at",
        DateTime(timezone=True),
        server_default=text("now()"),
        nullable=False,
    ),
    Column(
        "hash_password",
        String(),
        nullable=False,
    ),
    Column(
        "status",
        String(),
        nullable=False,
    ),
)
