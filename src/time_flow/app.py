"""App file."""

from typing import Annotated

from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncConnection

from .auth.view import router as auth_router
from .db.database import lifespan
from .db.dependencies import get_conn
from .utils import get_settings
from .utils.log import get_logger

settings = get_settings()

log = get_logger(name=__name__, settings=settings.LOGGING)


app = FastAPI(lifespan=lifespan)
log.info("App started")

app.include_router(
    auth_router,
)


@app.get("/")
async def read_root(
    conn: Annotated[AsyncConnection, Depends(get_conn)],
) -> str:
    """Test root."""
    result = await conn.execute(text("SELECT NOW() AS now"))
    row = result.fetchone()

    now_value = row.now if row is not None else "no data"
    return f"Now is | {now_value}"
