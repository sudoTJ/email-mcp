import asyncio
import logging
import os
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from api.routes.base_route import api_router
from api.routes.mcp_route import start_mcp_server

logger = logging.getLogger(__name__)


def build_app() -> FastAPI:
    """Build and configure the FastAPI application."""

    # Create FastAPI app
    app = FastAPI(
        title="Sample fastAPI server",
        lifespan=lifespan
    )

    # Include mcp router
    app.include_router(
        api_router,
    )

    return app

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None,None]:
    asyncio.create_task(start_mcp_server())

    yield