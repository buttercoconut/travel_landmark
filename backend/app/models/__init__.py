"""Database configuration and session management.

Uses SQLAlchemy with a SQLite database for simplicity. In a production
environment you would replace the SQLite URL with a PostgreSQL or other
database.
"""

from __future__ import annotations

from pathlib import Path
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Base class for ORM models
Base = declarative_base()

# Database URL – replace with your production DB URL
DATABASE_URL = "sqlite:///./landmarks.db"

# Create engine and session factory
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get DB session

def get_db() -> Generator:
    """Yield a SQLAlchemy session and close it after use."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)
