"""Main application entry point for the Travel Landmark API.

This module sets up the FastAPI application, configures the database, and
includes the routers that expose the CRUD endpoints for landmarks.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config.settings import Settings
from .routers import landmark_router

# Load settings
settings = Settings()

# Create FastAPI app
app = FastAPI(
    title="Travel Landmark API",
    description="API for managing travel landmarks.",
    version="0.1.0",
)

# CORS configuration (allow all for demo purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(landmark_router, prefix="/landmarks", tags=["landmarks"])

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Travel Landmark API!"}
