"""App file."""

from typing import Annotated

import asyncpg
from fastapi import Depends, FastAPI

from .db.database import get_conn, lifespan
from .utils import get_settings
from .utils.log import get_logger

settings = get_settings()

log = get_logger(name=__name__, settings=settings.LOGGING)


app = FastAPI(lifespan=lifespan)
log.info("App started")


@app.get("/")
async def read_root(
    conn: Annotated[asyncpg.Connection, Depends(get_conn)],
) -> str:
    """Read root."""
    row = await conn.fetchrow("SELECT NOW() AS now;")
    now_value = row["now"] if row else "no data"
    return f"Now is | {now_value}"
