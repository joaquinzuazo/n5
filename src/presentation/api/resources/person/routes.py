from typing import List

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from src.domain import PersonExists, PersonIDNotFound
from src.presentation.api.di.stub import person_usecase_stub
from src.presentation.api.resources.commons.response_model import ResponseModel
from src.presentation.api.resources.person.request_model import (
    PersonCreate,
    PersonUpdate,
)
from src.presentation.api.resources.person.response_model import PersonReadModel

person_router = APIRouter()


@person_router.get("/person", response_model=ResponseModel[List[PersonReadModel]])
def get_persons(
    person_usecase=Depends(person_usecase_stub),
):
    try:
        list_person = person_usecase.get_persons()
        return ResponseModel(
            error=False,
            message="List of persons",
            data=list_person,
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": str(e)},
        )


@person_router.post("/person", response_model=ResponseModel)
def create_person(
    person: PersonCreate,
    person_usecase=Depends(person_usecase_stub),
):
    try:
        person_usecase.create_person(person)
        return ResponseModel(
            error=False,
            message="Person created successfully",
            data=[],
        )
    except PersonExists as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=ResponseModel(error=True, message=str(e), data={}).model_dump(),
        )


@person_router.put("/person/{id}", response_model=ResponseModel)
def update_person(
    id: int,
    person: PersonUpdate,
    person_usecase=Depends(person_usecase_stub),
):
    try:
        person_usecase.update_person(id, person)
        return ResponseModel(
            error=False,
            message="Person updated successfully",
            data=[],
        )
    except PersonIDNotFound as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=ResponseModel(error=True, message=str(e), data={}).model_dump(),
        )


@person_router.delete("/person/{id}", response_model=ResponseModel)
def delete_person(
    id: str,
    person_usecase=Depends(person_usecase_stub),
):
    try:
        person_usecase.delete_person(id)
        return ResponseModel(
            error=False,
            message="Person deleted successfully",
            data=[],
        )
    except PersonIDNotFound as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=ResponseModel(error=True, message=str(e), data={}).model_dump(),
        )
