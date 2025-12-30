"""Hasher."""

import bcrypt


class PasswordHasher:
    """Password hasher."""

    def hash(self, password: str) -> str:
        """Hashing password.

        Parameters
        ----------
        password : str
            string

        Returns
        -------
        str
            hash
        """
        salt = bcrypt.gensalt()
        hashed: bytes = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed.decode("utf-8")

    def verify(self, password: str, hashed: str) -> bool:
        """Verify string and hash.

        Parameters
        ----------
        password : str
            string
        hashed : str
            hash string

        Returns
        -------
        bool
            equivalence pw ans hash
        """
        return bool(bcrypt.checkpw(password.encode("utf-8"),
                                   hashed.encode("utf-8")))

