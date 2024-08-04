from abc import ABC, abstractmethod

from src.domain import OfficerNotFound, OfficerRepository
from src.presentation.api.resources.officer.request_model import OfficierLogin


class OfficerUseCase(ABC):
    @abstractmethod
    def login_officer(self, infraction: OfficierLogin) -> None:
        raise NotImplementedError()


class OfficerUseCaseImpl(OfficerUseCase):
    def __init__(
        self,
        officer_repository: OfficerRepository,
    ):
        self.officer_repository = officer_repository

    def login_officer(self, data: OfficierLogin) -> None:
        try:
            officer = self.officer_repository.get_officer_by_badge(data.badge_number)
            if not officer or not officer.verify_password(data.password):
                raise OfficerNotFound
            print("Officer logged in")
        except Exception as e:
            raise e
