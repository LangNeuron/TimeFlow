"""
Logging infrastructure module.

All logging parameters are injected via get_logger
to support external configuration management.
"""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .conf import LoggingSettings


def get_logger(*, name: str, settings: LoggingSettings) -> logging.Logger:
    """Create a logger using a LoggingSettings instance."""
    logger = logging.getLogger(name)
    logger.setLevel(settings.level)
    logger.propagate = False

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt=settings.FORMAT,
        datefmt=settings.DATE_FORMAT,
    )

    log_dir = Path(settings.log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)

    common_handler = RotatingFileHandler(
        filename=log_dir / settings.COMMON_LOG_FILENAME,
        maxBytes=settings.COMMON_MAX_BYTES,
        backupCount=settings.COMMON_BACKUP_COUNT,
        encoding="utf-8",
    )
    common_handler.setLevel(settings.level)
    common_handler.setFormatter(formatter)

    personal_filename = f"{name.replace('.', '_')}.log"
    personal_handler = RotatingFileHandler(
        filename=log_dir / personal_filename,
        maxBytes=settings.PERSONAL_MAX_BYTES,
        backupCount=settings.PERSONAL_BACKUP_COUNT,
        encoding="utf-8",
    )
    personal_handler.setLevel(settings.level)
    personal_handler.setFormatter(formatter)

    logger.addHandler(common_handler)
    logger.addHandler(personal_handler)

    return logger
