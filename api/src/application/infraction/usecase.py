from abc import ABC, abstractmethod

from src.domain import (
    InfractionEntity,
    InfractionRepository,
    PersonEmailNotFound,
    PersonRepository,
    VehicleNotFound,
    VehicleRepository,
)
from src.presentation.api.resources.infraction.request_model import (
    InfractionCreateRequest,
)


class InfractionUseCase(ABC):
    @abstractmethod
    def create_infraction(
        self, infraction: InfractionCreateRequest
    ) -> InfractionEntity:
        raise NotImplementedError()

    @abstractmethod
    def get_infractions_by_person_email(self, email: str) -> list[InfractionEntity]:
        raise NotImplementedError()


class InfractionUseCaseImpl(InfractionUseCase):
    def __init__(
        self,
        infraction_repository: InfractionRepository,
        person_repository: PersonRepository,
        vehicle_repsoitory: VehicleRepository,
    ):
        self.infraction_repository = infraction_repository
        self.person_repository = person_repository
        self.vehicle_repository = vehicle_repsoitory

    def _map_to_infraction_domain(
        self, infraction: InfractionCreateRequest
    ) -> InfractionEntity:
        return InfractionEntity(
            id=None,
            license_plate=infraction.license_plate,
            timestamp=infraction.timestamp,
            comments=infraction.comments,
        )

    def create_infraction(
        self, infraction: InfractionCreateRequest
    ) -> InfractionEntity:
        try:
            vehicle = self.vehicle_repository.get_vehicle_by_license(
                infraction.license_plate
            )
            if not vehicle:
                raise VehicleNotFound
            infraction_domain = self._map_to_infraction_domain(infraction)
            self.infraction_repository.create_infraction(infraction_domain)
        except Exception as e:
            raise e

    def get_infractions_by_person_email(self, email: str) -> list[InfractionEntity]:
        try:
            person = self.person_repository.get_person_by_email(email)
            if not person:
                raise PersonEmailNotFound

            infractions = self.infraction_repository.get_infractions_by_user_id(
                person.id
            )
            return infractions
        except Exception as e:
            raise e
