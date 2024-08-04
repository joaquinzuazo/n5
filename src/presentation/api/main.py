from fastapi import FastAPI

from src.presentation.api.di import setup_di
from fastapi.middleware.cors import CORSMiddleware
from src.presentation.api.resources.commons.exceptions_handlers import (
    generic_exception_handler,
)
from src.presentation.api.resources.infraction.routes import router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Challenger n5",
        description="Sistema de registro de infracciones de tránsito",
        version="1.0.0",
        docs_url="/docs",
        openapi_url="/openapi.json",
    )

    app.include_router(router)

    app.add_exception_handler(Exception, generic_exception_handler)

    setup_di(app)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app

app = create_app()
