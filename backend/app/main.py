from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.metrics import router as metrics_router
from app.api.health import router as health_router
#from app.api.forecast import router as forecast_router
#from app.api import recommendations
from app.api import copilot

from app.api.analysis import router as analysis_router

from app.core.config import settings
from app.core.logging import logger

from app.exceptions.handlers import register_exception_handlers

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="AI Powered Cloud Resource Optimization Copilot",
)


register_exception_handlers(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    health_router,
    prefix=settings.API_PREFIX,
)

app.include_router(
    metrics_router,
    prefix=settings.API_PREFIX,
)
# app.include_router(
#     forecast_router,
#     prefix=settings.API_PREFIX,
# )
# app.include_router(
#     recommendations.router,
#     prefix="/api/v1"
# )
app.include_router(
    copilot.router,
    prefix="/api/v1"
)

app.include_router(
    analysis_router,
    prefix=settings.API_PREFIX
)


@app.on_event("startup")
async def startup_event():
    logger.info("Cloud Copilot Backend Started")


@app.get("/", tags=["Home"])
async def home():
    return {
        "application": settings.APP_NAME,
        "version": settings.VERSION,
        "status": "Running"
    }