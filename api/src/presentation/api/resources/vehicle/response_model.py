from pydantic import BaseModel


class VehicleReadModel(BaseModel):
    id: int
    license_plate: str
    brand: str
    color: str
    owner_id: int
