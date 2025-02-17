from typing import Optional

from sqlalchemy.orm import Session
from src.domain import VehicleEntity, VehicleRepository
from src.infrastructure.database.models import VehicleModel


class VehicleRepositoryImpl(VehicleRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_vehicle_by_license(self, license: str) -> Optional[VehicleEntity]:
        try:
            vehicle = (
                self.session.query(VehicleModel)
                .filter(VehicleModel.license_plate == license)
                .first()
            )
            if not vehicle:
                return None
            return vehicle.to_entity()
        except Exception as e:
            raise e

    def get_vehicles(self) -> list[VehicleEntity]:
        try:
            return [
                vehicle.to_entity()
                for vehicle in self.session.query(VehicleModel).all()
            ]
        except Exception as e:
            raise e

    def get_vehicle_by_id(self, id: str) -> Optional[VehicleEntity]:
        try:
            vehicle = (
                self.session.query(VehicleModel).filter(VehicleModel.id == id).first()
            )
            if not vehicle:
                return None
            return vehicle.to_entity()
        except Exception as e:
            raise e

    def create_vehicle(self, vehicle: VehicleEntity) -> VehicleEntity:
        try:
            vehicle_model = VehicleModel.from_entity(vehicle)
            self.session.add(vehicle_model)
            self.session.commit()
            return vehicle_model.to_entity()
        except Exception as e:
            raise e

    def update_vehicle(self, vehicle: VehicleEntity) -> VehicleEntity:
        try:
            vehicle_model = (
                self.session.query(VehicleModel)
                .filter(VehicleModel.id == vehicle.id)
                .first()
            )
            vehicle_model.license_plate = vehicle.license_plate
            vehicle_model.owner_id = vehicle.owner_id
            self.session.commit()
            return vehicle_model.to_entity()
        except Exception as e:
            raise e

    def delete_vehicle(self, id: str) -> None:
        try:
            vehicle = (
                self.session.query(VehicleModel).filter(VehicleModel.id == id).first()
            )
            self.session.delete(vehicle)
            self.session.commit()
        except Exception as e:
            raise e
