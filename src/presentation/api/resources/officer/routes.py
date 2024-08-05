from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from src.domain import OfficerBadgeExists, OfficerNotFound
from src.infrastructure.database.models.models import RoleEnum
from src.presentation.api.di.stub import get_current_officer_stub, officer_usecase_stub
from src.presentation.api.resources.commons.response_model import ResponseModel
from src.presentation.api.resources.officer.request_model import (
    OfficerCreate,
    OfficerLogin,
    OfficerUpdate,
)
from src.presentation.api.resources.officer.response_model import Token

officer_router = APIRouter()


@officer_router.post("/login", response_model=ResponseModel[Token])
def officer_login(
    data: OfficerLogin,
    usecase=Depends(officer_usecase_stub),
):
    try:
        access_token, refresh_token = usecase.login_officer(data)
        return ResponseModel(
            error=False,
            message="Officer logged in successfully",
            data=Token(access_token=access_token, refresh_token=refresh_token),
        )
    except OfficerNotFound as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=ResponseModel(error=True, message=str(e), data={}).model_dump(),
        )


@officer_router.post("/officer", response_model=ResponseModel)
def create_officer(
    data: OfficerCreate,
    usecase=Depends(officer_usecase_stub),
    current_officer=Depends(get_current_officer_stub),
):
    try:
        if RoleEnum(current_officer.role) != RoleEnum.ADMIN:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content=ResponseModel(
                    error=True, message="Unauthorized", data={}
                ).model_dump(),
            )
        usecase.create_officer(data)
        return ResponseModel(
            error=False,
            message="Officer created successfully",
            data=[],
        )
    except OfficerNotFound as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=ResponseModel(error=True, message=str(e), data={}).model_dump(),
        )


@officer_router.put("/officer/{id}", response_model=ResponseModel)
def update_officer(
    id: str,
    data: OfficerUpdate,
    usecase=Depends(officer_usecase_stub),
    current_officer=Depends(get_current_officer_stub),
):
    try:
        badge = current_officer.get("badge")
        usecase.update_officer(id=id, badge=badge, update_officer=data)
        return ResponseModel(
            error=False,
            message="Officer updated successfully",
            data=[],
        )
    except (OfficerNotFound, OfficerBadgeExists) as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=ResponseModel(error=True, message=str(e), data={}).model_dump(),
        )


@officer_router.delete("/officer/{id}", response_model=ResponseModel)
def delete_officer(
    id: str,
    usecase=Depends(officer_usecase_stub),
    current_officer=Depends(get_current_officer_stub),
):
    try:
        badge = current_officer.get("badge")
        usecase.delete_officer(id=id, badge=badge)
        return ResponseModel(
            error=False,
            message="Officer deleted successfully",
            data=[],
        )
    except OfficerNotFound as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=ResponseModel(error=True, message=str(e), data={}).model_dump(),
        )
