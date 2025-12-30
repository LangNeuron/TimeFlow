"""Database services."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
)

from time_flow.utils import get_settings

settings = get_settings()


def create_engine() -> AsyncEngine:
    """Create Engine."""
    return create_async_engine(
        settings.DB.url_async,
        pool_size=settings.DB.min_size,
        max_overflow=settings.DB.max_size - settings.DB.min_size,
        pool_pre_ping=True,
    )


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Lifespan fastapi."""
    engine: AsyncEngine = create_engine()
    app.state.db_engine = engine
    yield
    await engine.dispose()
