from datetime import datetime
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from src.domain.vehicle.entity import VehicleEntity


class InfractionEntity:
    def __init__(
        self,
        id: Optional[int],
        license_plate: str,
        timestamp: datetime,
        comments: str,
        vehicle: Optional["VehicleEntity"] = None,
    ):
        self.id = id
        self.license_plate = license_plate
        self.timestamp = timestamp
        self.comments = comments
        self.vehicle = vehicle
