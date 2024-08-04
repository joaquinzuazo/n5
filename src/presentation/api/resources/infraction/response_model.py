from datetime import datetime

from pydantic import BaseModel


class VehicleResponse(BaseModel):
    id: int
    license_plate: str
    brand: str
    color: str


class InfractionResponse(BaseModel):
    id: int
    timestamp: datetime
    comments: str
    vehicle: VehicleResponse
