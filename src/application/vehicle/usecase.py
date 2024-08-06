from abc import ABC, abstractmethod
from typing import Optional

from src.domain import (
    OwnerIDNotFound,
    PersonRepository,
    VehicleAlreadyExists,
    VehicleEntity,
    VehicleNotFound,
    VehicleRepository,
)
from src.presentation.api.resources.vehicle.request_model import (
    VehicleCreate,
    VehicleUpdate,
)


class VehicleUseCase(ABC):
    @abstractmethod
    def get_vehicle_by_license(self, license_plate: str) -> Optional[VehicleEntity]:
        raise NotImplementedError()

    @abstractmethod
    def get_vehicle_by_id(self, id: int) -> Optional[VehicleEntity]:
        raise NotImplementedError()

    @abstractmethod
    def get_vehicles(self) -> list[VehicleEntity]:
        raise NotImplementedError()

    @abstractmethod
    def create_vehicle(self, vehicle: VehicleCreate) -> None:
        raise NotImplementedError()

    @abstractmethod
    def update_vehicle(self, id: int, vehicle: VehicleUpdate) -> None:
        raise NotImplementedError()

    @abstractmethod
    def delete_vehicle(self, id: int) -> None:
        raise NotImplementedError()


class VehicleUseCaseImpl(VehicleUseCase):
    def __init__(
        self, vehicle_repository: VehicleRepository, person_repository: PersonRepository
    ):
        self.vehicle_repository = vehicle_repository
        self.person_repository = person_repository

    def get_vehicle_by_license(self, license_plate: str) -> Optional[VehicleEntity]:
        try:
            return self.vehicle_repository.get_vehicle_by_license(license_plate)
        except Exception as e:
            raise e

    def get_vehicle_by_id(self, id: int) -> Optional[VehicleEntity]:
        try:
            return self.vehicle_repository.get_vehicle_by_id(id)
        except Exception as e:
            raise e

    def get_vehicles(self) -> list[VehicleEntity]:
        try:
            return self.vehicle_repository.get_vehicles()
        except Exception as e:
            raise e

    def create_vehicle(self, vehicle: VehicleCreate) -> None:
        try:
            vehicle_exists = self.vehicle_repository.get_vehicle_by_license(
                vehicle.license_plate
            )
            if vehicle_exists:
                raise VehicleAlreadyExists

            person = self.person_repository.get_person_by_id(vehicle.owner_id)
            if not person:
                raise OwnerIDNotFound

            vehicle = VehicleEntity(
                id=None,
                license_plate=vehicle.license_plate,
                brand=vehicle.brand,
                color=vehicle.color,
                owner_id=vehicle.owner_id,
            )
            self.vehicle_repository.create_vehicle(vehicle)
        except Exception as e:
            raise e

    def update_vehicle(self, id: int, vehicle: VehicleUpdate) -> None:
        try:
            vehicle_exists = self.vehicle_repository.get_vehicle_by_id(id)
            if not vehicle_exists:
                raise VehicleNotFound

            if vehicle.license_plate != vehicle_exists.license_plate:
                vehicle_exists = self.vehicle_repository.get_vehicle_by_license(
                    vehicle.license_plate
                )
                if vehicle_exists:
                    raise VehicleAlreadyExists

            person = self.person_repository.get_person_by_id(vehicle.owner_id)
            if not person:
                raise OwnerIDNotFound

            vehicle = VehicleEntity(
                id=id,
                license_plate=vehicle.license_plate,
                brand=vehicle.brand,
                color=vehicle.color,
                owner_id=vehicle.owner_id,
            )

            self.vehicle_repository.update_vehicle(vehicle)
        except Exception as e:
            raise e

    def delete_vehicle(self, id: int) -> None:
        try:
            vehicle_exists = self.vehicle_repository.get_vehicle_by_id(id)
            if not vehicle_exists:
                raise VehicleNotFound
            self.vehicle_repository.delete_vehicle(id)
        except Exception as e:
            raise e
