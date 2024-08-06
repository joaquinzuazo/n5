from typing import List

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from src.domain import OwnerIDNotFound, VehicleAlreadyExists, VehicleNotFound
from src.presentation.api.di.stub import vehicle_usecase_stub
from src.presentation.api.resources.commons.response_model import ResponseModel
from src.presentation.api.resources.officer.routes import get_current_officer_stub
from src.presentation.api.resources.vehicle.request_model import (
    VehicleCreate,
    VehicleUpdate,
)
from src.presentation.api.resources.vehicle.response_model import VehicleReadModel

vehicle_router = APIRouter()


@vehicle_router.get("/vehicle", response_model=ResponseModel[List[VehicleReadModel]])
def get_vehicles(
    vehicle_usecase=Depends(vehicle_usecase_stub),
    _=Depends(get_current_officer_stub),
):
    vehicles = vehicle_usecase.get_vehicles()
    return ResponseModel(
        error=False,
        message="Vehicles fetched successfully",
        data=vehicles,
    )


@vehicle_router.post("/vehicle", response_model=ResponseModel)
def create_vehicle(
    vehicle: VehicleCreate,
    vehicle_usecase=Depends(vehicle_usecase_stub),
    _=Depends(get_current_officer_stub),
):
    try:
        vehicle_usecase.create_vehicle(vehicle)
        return ResponseModel(
            error=False,
            message="Vehicle created successfully",
            data=[],
        )
    except (VehicleAlreadyExists, OwnerIDNotFound) as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=ResponseModel(error=True, message=str(e), data={}).model_dump(),
        )


@vehicle_router.put("/vehicle/{id}", response_model=ResponseModel)
def update_vehicle(
    id: int,
    vehicle: VehicleUpdate,
    vehicle_usecase=Depends(vehicle_usecase_stub),
    _=Depends(get_current_officer_stub),
):
    try:
        vehicle_usecase.update_vehicle(id, vehicle)
        return ResponseModel(
            error=False,
            message="Vehicle updated successfully",
            data=[],
        )
    except (VehicleNotFound, OwnerIDNotFound, VehicleAlreadyExists) as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=ResponseModel(error=True, message=str(e), data={}).model_dump(),
        )


@vehicle_router.delete("/vehicle/{id}", response_model=ResponseModel)
def delete_vehicle(
    id: int,
    vehicle_usecase=Depends(vehicle_usecase_stub),
    _=Depends(get_current_officer_stub),
):
    try:
        vehicle_usecase.delete_vehicle(id)
        return ResponseModel(
            error=False,
            message="Vehicle deleted successfully",
            data=[],
        )
    except VehicleNotFound as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=ResponseModel(error=True, message=str(e), data={}).model_dump(),
        )
