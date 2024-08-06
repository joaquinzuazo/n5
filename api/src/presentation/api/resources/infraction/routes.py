from typing import List

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from src.application.infraction.usecase import InfractionUseCase
from src.domain import PersonEmailNotFound, VehicleNotFound
from src.presentation.api.di.stub import (
    get_current_officer_stub,
    infraction_usecase_stub,
)
from src.presentation.api.resources.commons.response_model import ResponseModel
from src.presentation.api.resources.infraction.request_model import (
    InfractionCreateRequest,
)
from src.presentation.api.resources.infraction.response_model import InfractionResponse

infractions_router = APIRouter()


@infractions_router.post("/infractions/", response_model=ResponseModel)
def create_infraction_endpoint(
    infraction: InfractionCreateRequest,
    usecase: InfractionUseCase = Depends(infraction_usecase_stub),
    _: dict = Depends(get_current_officer_stub),
):
    try:
        usecase.create_infraction(infraction)
        return ResponseModel(
            error=False, message="Infraction created successfully", data=[]
        )
    except VehicleNotFound as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=ResponseModel(error=True, message=str(e), data=[]).dict(),
        )


@infractions_router.get(
    "/infractions/report", response_model=ResponseModel[List[InfractionResponse]]
)
def generate_infraction_report(
    email: str, usecase: InfractionUseCase = Depends(infraction_usecase_stub)
):
    try:
        infractions = usecase.get_infractions_by_person_email(email)
        return ResponseModel(
            error=False, message="Report generated successfully", data=infractions
        )
    except PersonEmailNotFound as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=ResponseModel(error=True, message=str(e), data=[]).dict(),
        )
