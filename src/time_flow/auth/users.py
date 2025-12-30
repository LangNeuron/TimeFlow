"""User CRUD."""

from datetime import UTC, datetime

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncConnection

from time_flow.db.tables import user

from .models import CreateUser, UserDB


class User:
    """User CRUD service."""

    @staticmethod
    async def create(user_cred: CreateUser, conn: AsyncConnection) -> UserDB:
        """Create user in database."""
        query = (
            user.insert()
            .values(
                name=user_cred.name,
                email=user_cred.email,
                hash_password=user_cred.hash_password,
                status=user_cred.status,
                created_at=datetime.now(UTC),
            )
            .returning(
                user.c.uid,
                user.c.name,
                user.c.email,
                user.c.hash_password,
                user.c.status,
            )
        )
        result = await conn.execute(query)
        row = result.first()
        if row is None:
            msg = "Invalid user cred"
            raise ValueError(msg)
        return UserDB(**row._asdict())

    @staticmethod
    async def _get_by_email(
        email: str,
        conn: AsyncConnection,
    ) -> UserDB | None:
        """Get user by email."""
        query = select(user).where(user.c.email == email)
        result = await conn.execute(query)
        row = result.first()
        return UserDB(**row._asdict()) if row else None

    @staticmethod
    async def _get_by_uid(uid: int, conn: AsyncConnection) -> UserDB | None:
        """Get user by id."""
        query = select(user).where(user.c.uid == uid)
        result = await conn.execute(query)
        row = result.first()
        return UserDB(**row._asdict()) if row else None

    @staticmethod
    async def update(
        uid: int,
        values: dict[str, str | int],
        conn: AsyncConnection,
    ) -> UserDB | None:
        """Update user fields."""
        query = (
            update(user)
            .where(user.c.uid == uid)
            .values(**values)
            .returning(
                user.c.uid,
                user.c.name,
                user.c.email,
                user.c.hash_password,
                user.c.status,
            )
        )
        result = await conn.execute(query)
        row = result.first()
        return UserDB(**row._asdict()) if row else None

    @staticmethod
    async def delete(uid: int, conn: AsyncConnection) -> bool:
        """Delete user by uid."""
        query = delete(user).where(user.c.uid == uid)
        result = await conn.execute(query)
        rowcount: int = result.rowcount
        return rowcount > 0
