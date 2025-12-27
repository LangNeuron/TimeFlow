"""Settings."""

from functools import lru_cache
from pathlib import Path

from .conf import Config, configure

BASE_DIR = Path(__file__).resolve().parents[3]


@lru_cache(maxsize=1)
def get_settings() -> Config:
    """Get settings."""
    return configure(
        json_file_settings=BASE_DIR / "config" / "config.json",
        env_file_settings=BASE_DIR / "config" / ".env",
    )
