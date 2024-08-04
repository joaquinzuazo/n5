from typing import Optional

from sqlalchemy.orm import Session

from src.domain import VehicleEntity, VehicleRepository
from src.infrastructure.database.models import VehicleModel


class VehicleRepositoryImpl(VehicleRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_vehicle_by_license(self, license: str) -> Optional[VehicleEntity]:
        vehicle = (
            self.session.query(VehicleModel)
            .filter(VehicleModel.license_plate == license)
            .first()
        )
        if not vehicle:
            return None
        return vehicle.to_entity()
