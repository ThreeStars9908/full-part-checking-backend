# app/main.py
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api import check_body
from model.model import load_model


# Custom logging configuration
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.CRITICAL  # Disables lower levels (INFO, DEBUG, etc.)
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    load_model()
    yield


app = FastAPI(
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
    redoc_url=None,
    lifespan=lifespan,
)

# Include the map data router
app.include_router(check_body.router, prefix="/api")
