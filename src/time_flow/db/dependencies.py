"""Depends."""

from collections.abc import AsyncGenerator

from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncConnection


async def get_conn(
    request: Request,
) -> AsyncGenerator[AsyncConnection, None]:
    """Get async connection to DB."""
    engine = request.app.state.db_engine

    async with engine.begin() as conn:
        yield conn
