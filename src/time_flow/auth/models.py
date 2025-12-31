"""Models of the user."""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr


class CreateUser(BaseModel):
    """Create user credentials."""

    email: EmailStr
    name: str
    hash_password: str
    status: str = "pending"


class Register(BaseModel):
    """Register model."""

    email: EmailStr
    name: str
    password: str


class Login(BaseModel):
    """Login model."""

    email: EmailStr
    password: str


class UserDB(BaseModel):
    """User cred in database."""

    uid: UUID
    email: EmailStr
    name: str
    hash_password: str
    status: str
    created_at: datetime
