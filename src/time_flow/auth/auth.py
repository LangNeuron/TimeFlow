"""Authorization module."""

from sqlalchemy.ext.asyncio import AsyncConnection

from time_flow.utils.hasher import PasswordHasher

from .models import CreateUser, Register
from .users import User

hasher = PasswordHasher()


class Auth:
    """Auth module."""

    def __init__(self, user_manager: User) -> None:
        """Init."""
        self.user_manager = user_manager

    async def register(
        self,
        user_cred: Register,
        conn: AsyncConnection,
    ) -> None:
        """Need add timer for auth."""
        user = CreateUser(
            email=user_cred.email,
            name=user_cred.name,
            hash_password=hasher.hash(user_cred.password),
            status="pending",
        )
        await self.user_manager.create(user, conn)
