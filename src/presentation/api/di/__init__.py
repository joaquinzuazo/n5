from fastapi import FastAPI
from src.presentation.api.di.provider import infraction_usecase, officer_login_usecase
from src.presentation.api.di.stub import (
    infraction_usecase_stub,
    officer_login_usecase_stub,
)


def setup_di(app: FastAPI) -> None:
    app.dependency_overrides[infraction_usecase_stub] = infraction_usecase
    app.dependency_overrides[officer_login_usecase_stub] = officer_login_usecase
