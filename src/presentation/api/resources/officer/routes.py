from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from src.domain import OfficerNotFound
from src.presentation.api.di.stub import officer_login_usecase_stub
from src.presentation.api.resources.commons.response_model import ResponseModel
from src.presentation.api.resources.officer.request_model import OfficierLogin
from src.presentation.api.resources.officer.response_model import Token

officer_router = APIRouter()


@officer_router.post("/login", response_model=ResponseModel[Token])
def officer_login(
    data: OfficierLogin,
    usecase=Depends(officer_login_usecase_stub),
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
            content=ResponseModel(error=True, message=str(e), data={}).dict(),
        )
