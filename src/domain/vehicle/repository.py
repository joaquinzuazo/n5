from abc import ABC, abstractmethod
from typing import Optional

from src.domain import VehicleEntity


class VehicleRepository(ABC):
    @abstractmethod
    def get_vehicle_by_license(self, license: str) -> Optional[VehicleEntity]:
        raise NotImplementedError()

    @abstractmethod
    def get_vehicles(self) -> list[VehicleEntity]:
        raise NotImplementedError()

    @abstractmethod
    def get_vehicle_by_id(self, id: str) -> Optional[VehicleEntity]:
        raise NotImplementedError()

    @abstractmethod
    def create_vehicle(self, vehicle: VehicleEntity) -> VehicleEntity:
        raise NotImplementedError()

    @abstractmethod
    def update_vehicle(self, vehicle: VehicleEntity) -> VehicleEntity:
        raise NotImplementedError()

    @abstractmethod
    def delete_vehicle(self, id: str) -> None:
        raise NotImplementedError()
