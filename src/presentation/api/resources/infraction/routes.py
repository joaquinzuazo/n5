from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from src.application.infraction.usecase import InfractionUseCase
from src.domain import PersonNotFound, VehicleNotFound
from src.presentation.api.di.stub import infraction_usecase_stub
from src.presentation.api.resources.commons.response_model import ResponseModel
from src.presentation.api.resources.infraction.request_model import (
    InfractionCreateRequest,
)
from src.presentation.api.resources.infraction.response_model import InfractionResponse

router = APIRouter()


@router.post("/infractions/", response_model=ResponseModel)
def create_infraction_endpoint(
    infraction: InfractionCreateRequest,
    usecase: InfractionUseCase = Depends(infraction_usecase_stub),
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


@router.get("/infractions/report", response_model=ResponseModel[InfractionResponse])
def generate_infraction_report(
    email: str, usecase: InfractionUseCase = Depends(infraction_usecase_stub)
):
    try:
        infractions = usecase.get_infractions_by_person_email(email)
        return ResponseModel(
            error=False, message="Report generated successfully", data=infractions
        )
    except PersonNotFound as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=ResponseModel(error=True, message=str(e), data=[]).dict(),
        )
