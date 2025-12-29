"""Create database."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any

import asyncpg
from fastapi import FastAPI, Request

from time_flow.utils import get_settings

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[Any, Any]:
    """Lifespan."""
    app.state.db_pool = await asyncpg.create_pool(
        user=settings.DB.user,
        password=settings.DB.password,
        database=settings.DB.name,
        host=settings.DB.host,
        port=settings.DB.port,
        min_size=settings.DB.min_size,
        max_size=settings.DB.max_size,
    )
    yield
    await app.state.db_pool.close()


async def get_conn(
    request: Request,
) -> AsyncGenerator[asyncpg.Connection, None]:
    """Get connection."""
    async with request.app.state.db_pool.acquire() as conn:
        yield conn
