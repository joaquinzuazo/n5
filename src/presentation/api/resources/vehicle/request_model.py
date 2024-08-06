from pydantic import BaseModel


class VehicleBaseModel(BaseModel):
    license_plate: str
    brand: str
    color: str


class VehicleCreate(VehicleBaseModel):
    owner_id: int


class VehicleUpdate(VehicleCreate):
    pass
