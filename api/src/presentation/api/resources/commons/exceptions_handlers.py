from typing import List

from fastapi import Request, status
from fastapi.responses import JSONResponse
from src.presentation.api.resources.commons.response_model import ResponseModel


def generic_exception_handler(_: Request, __: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=ResponseModel[List](
            error=True, message="An internal server error occurred", data=[]
        ).dict(),
    )
