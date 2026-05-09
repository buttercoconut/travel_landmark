"""Application settings using Pydantic BaseSettings.

This module centralises configuration such as database URL, debug flags,
and any other environment‑specific values.
"""

from pydantic import BaseSettings

class Settings(BaseSettings):
    # Example: DATABASE_URL = "sqlite:///./landmarks.db"
    DATABASE_URL: str = "sqlite:///./landmarks.db"
    DEBUG: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
