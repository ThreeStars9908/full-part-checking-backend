# app/main.py
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api import check_body
from model.model import load_model


# Suppress Uvicorn logs by setting the Uvicorn logger level to CRITICAL
logging.getLogger("uvicorn").setLevel(logging.CRITICAL)


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
