from fastapi import FastAPI
from src.presentation.api.di.provider import (
    infraction_usecase,
    officer_usecase,
    get_current_officer,
)
from src.presentation.api.di.stub import (
    infraction_usecase_stub,
    officer_usecase_stub,
    get_current_officer_stub,
)


def setup_di(app: FastAPI) -> None:
    app.dependency_overrides[infraction_usecase_stub] = infraction_usecase
    app.dependency_overrides[officer_usecase_stub] = officer_usecase
    app.dependency_overrides[get_current_officer_stub] = get_current_officer
