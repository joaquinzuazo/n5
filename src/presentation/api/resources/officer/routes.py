from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from src.presentation.api.di.stub import officer_login_usecase_stub
from src.presentation.api.resources.commons.response_model import ResponseModel
from src.presentation.api.resources.officer.request_model import OfficierLogin

officer_router = APIRouter()


@officer_router.post("/login", response_model=ResponseModel)
def officer_login(
    data: OfficierLogin,
    usecase=Depends(officer_login_usecase_stub),
):
    try:
        print(data)
        usecase.login_officer(data)
        return ResponseModel(error=False, message="Officer login successfully", data=[])
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=ResponseModel(error=True, message=str(e), data=[]).dict(),
        )
