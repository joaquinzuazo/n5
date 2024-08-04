from abc import ABC, abstractmethod

from src.domain import OfficerNotFound, OfficerRepository
from src.presentation.api.resources.officer.request_model import OfficierLogin
from src.utils.jwt import create_access_token, create_refresh_token


class OfficerUseCase(ABC):
    @abstractmethod
    def login_officer(self, infraction: OfficierLogin) -> tuple:
        raise NotImplementedError()


class OfficerUseCaseImpl(OfficerUseCase):
    def __init__(
        self,
        officer_repository: OfficerRepository,
    ):
        self.officer_repository = officer_repository

    def login_officer(self, data: OfficierLogin) -> tuple:
        try:
            officer = self.officer_repository.get_officer_by_badge(data.badge_number)
            if not officer or not officer.verify_password(data.password):
                raise OfficerNotFound

            access_token = create_access_token({"badge": officer.badge_number})
            refresh_token = create_refresh_token({"badge": officer.badge_number})

            return access_token, refresh_token
        except Exception as e:
            raise e
