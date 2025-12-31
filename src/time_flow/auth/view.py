"""View auth."""

from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncConnection

from time_flow.db.dependencies import get_conn

from .auth import Auth
from .models import Register
from .users import User

auth = Auth(User())

router = APIRouter()

@router.post("/api/register")
async def register(user_cred: Register,
                   conn: Annotated[AsyncConnection, Depends(get_conn)],
                   ) -> str:
    """Register api."""
    await auth.register(user_cred, conn)
    return "User Created" ## add redirect to verify code from email
