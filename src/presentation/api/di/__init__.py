from fastapi import FastAPI
from src.presentation.api.di.provider import infraction_usecase
from src.presentation.api.di.stub import infraction_usecase_stub


def setup_di(app: FastAPI) -> None:
    app.dependency_overrides[infraction_usecase_stub] = infraction_usecase
