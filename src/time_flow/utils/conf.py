"""Configuration module."""

import json
from logging import INFO
from pathlib import Path
from typing import Any

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class LoggingSettings(BaseSettings):
    """LoggingSettings."""

    level: int = INFO
    log_dir: Path = Path("logs")

    COMMON_LOG_FILENAME: str = "application.log"
    COMMON_MAX_BYTES: int = 10 * 1024 * 1024
    COMMON_BACKUP_COUNT: int = 10

    PERSONAL_MAX_BYTES: int = 5 * 1024 * 1024
    PERSONAL_BACKUP_COUNT: int = 5

    FORMAT: str = (
        "%(asctime)s | %(module)s | %(levelname)s | "
        "%(message)s | %(filename)s:%(lineno)d"
    )
    DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"

    model_config = SettingsConfigDict(
        extra="ignore",
        env_nested_delimiter="__",
        env_prefix="LOGGING_",
        case_sensitive=True,
        populate_by_name=True,
    )


class MailSettings(BaseSettings):
    """MailSettings gmail."""

    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USERNAME: str = ""
    SMTP_PASSWORD: str = ""
    DEFAULT_SENDER_EMAIL: str = ""
    DEFAULT_SENDER_NAME: str = ""

    USE_TLS: bool = True
    CHARSET: str = "utf-8"

    model_config = SettingsConfigDict(
        extra="ignore",
        env_nested_delimiter="__",
        populate_by_name=True,
        env_prefix="GMAIL_",
        case_sensitive=True,
    )


class DataBase(BaseModel):
    """Database settings."""

    user: str = ""
    password: str = ""
    host: str = "localhost"
    port: int = 5432
    name: str = ""
    min_size: int = 1
    max_size: int = 10

    model_config = SettingsConfigDict(
        extra="ignore",
        env_nested_delimiter="__",
        populate_by_name=True,
        env_prefix="DB_",
        case_sensitive=True,
    )


class Config(BaseSettings):
    """Config class for application settings."""

    NAME: str = "Time Flow"
    VERSION: str = "1.0.0"

    LOGGING: LoggingSettings = LoggingSettings()
    DB: DataBase = DataBase()
    GMAIL: MailSettings = MailSettings()

    model_config = SettingsConfigDict(
        extra="ignore",
        env_nested_delimiter="__",
        case_sensitive=True,
        populate_by_name=True,
    )

    def __init__(self, **data: Any) -> None:  # noqa: ANN401
        """Init Config."""
        super().__init__(**data)


def configure(
    json_file_settings: Path,
    env_file_settings: Path,
) -> Config:
    """Create config from files.

    Parameters
    ----------
    json_file_settings : Path
        json file path
    env_file_settings : Path
        env file path

    Returns
    -------
    Config
        Class of config
    """
    data = {}

    # 1. JSON (low priority)
    if json_file_settings:
        with Path.open(json_file_settings, mode="r", encoding="utf-8") as f:
            data.update(json.load(f))

    # 2. ENV + .env (high priority)
    return Config(
        **data,
        _env_file=env_file_settings,
    )
