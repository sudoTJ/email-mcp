import asyncio
import logging
import os
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from api.routes.base_route import api_router

logger = logging.getLogger(__name__)


def build_app() -> FastAPI:
    """Build and configure the FastAPI application."""

    # Create FastAPI app
    app = FastAPI(
        title="Sample fastAPI server",
    )

    # Include mcp router
    app.include_router(
        api_router,
    )

    return app