from fastapi import FastAPI

from app.routes import router

app = FastAPI(
    title="Lead Automation API",
    description="A lightweight FastAPI service for lead enrichment and message intent classification.",
    version="1.0.0",
)

app.include_router(router)
