from abc import ABC, abstractmethod

import bcrypt
from src.domain import (
    OfficerBadgeExists,
    OfficerEntity,
    OfficerLoginNotFound,
    OfficerNotFound,
    OfficerRepository,
)
from src.presentation.api.resources.officer.request_model import (
    OfficerCreate,
    OfficerLogin,
    OfficerUpdate,
)
from src.utils.jwt import create_access_token, create_refresh_token


class OfficerUseCase(ABC):
    @abstractmethod
    def login_officer(self, infraction: OfficerLogin) -> tuple:
        raise NotImplementedError()

    @abstractmethod
    def get_officer_by_badge(self, badge: str) -> OfficerEntity:
        raise NotImplementedError()
    
    @abstractmethod
    def get_officers(self) -> list:
        raise NotImplementedError()

    @abstractmethod
    def create_officer(self, infraction: OfficerCreate) -> None:
        raise NotImplementedError()

    @abstractmethod
    def update_officer(
        self, id: str, update_officer: OfficerUpdate
    ) -> None:
        raise NotImplementedError()

    @abstractmethod
    def delete_officer(self, id: str) -> None:
        raise NotImplementedError()


class OfficerUseCaseImpl(OfficerUseCase):
    def __init__(
        self,
        officer_repository: OfficerRepository,
    ):
        self.officer_repository = officer_repository

    def _generate_hashed_password(self, password: str) -> str:
        try:
            return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode(
                "utf-8"
            )
        except Exception as e:
            raise e

    def login_officer(self, data: OfficerLogin) -> tuple:
        try:
            officer = self.officer_repository.get_officer_by_badge(data.badge_number)
            if not officer or not officer.verify_password(data.password):
                raise OfficerLoginNotFound

            access_token = create_access_token({"badge": officer.badge_number})
            refresh_token = create_refresh_token({"badge": officer.badge_number})

            return access_token, refresh_token
        except Exception as e:
            raise e

    def get_officer_by_badge(self, badge: str) -> OfficerEntity:
        try:
            officer = self.officer_repository.get_officer_by_badge(badge)
            if not officer:
                raise OfficerNotFound

            return officer
        except Exception as e:
            raise e
        
    def get_officers(self) -> list:
        try:
            officers = self.officer_repository.get_officers()
            return officers
        except Exception as e:
            raise e

    def create_officer(self, data: OfficerCreate) -> None:
        try:
            officer = self.officer_repository.get_officer_by_badge(data.badge_number)
            if officer:
                raise OfficerBadgeExists

            hashed_password = self._generate_hashed_password(data.password)
            officer = OfficerEntity(
                id=None,
                badge_number=data.badge_number,
                name=data.name,
                hashed_password=hashed_password,
                role=data.role,
            )

            self.officer_repository.create_officer(officer)
        except Exception as e:
            raise e

    def update_officer(
        self, id: str, update_officer: OfficerUpdate
    ) -> None:
        try:
            officer = self.officer_repository.get_officer_by_id(id)
            if not officer:
                raise OfficerNotFound

            badge_exists = self.officer_repository.get_officer_by_badge(
                update_officer.badge_number
            )
            if badge_exists and badge_exists.id != id:
                raise OfficerBadgeExists

            self.officer_repository.update_officer(id=id, officer=update_officer)
        except Exception as e:
            raise e

    def delete_officer(self, id: str) -> None:
        try:
            officer = self.officer_repository.get_officer_by_id(id)
            if not officer:
                raise OfficerNotFound

            self.officer_repository.delete_officer(id)
        except Exception as e:
            raise e
