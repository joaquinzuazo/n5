from typing import Optional


class VehicleEntity:
    def __init__(
        self,
        id: Optional[int],
        license_plate: str,
        brand: str,
        color: str,
        owner_id: int,
    ):
        self.id = id
        self.license_plate = license_plate
        self.brand = brand
        self.color = color
        self.owner_id = owner_id
