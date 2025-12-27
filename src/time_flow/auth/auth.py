"""Authorization module."""

from time_flow.users.manager import UserManager


class Auth:
    """Auth module."""

    def __init__(self, user_manager: UserManager) -> None:
        """Init."""
        self.user_manager = user_manager
