from abc import ABC, abstractmethod
from typing import Optional

from src.domain import OfficerEntity


class OfficerRepository(ABC):
    @abstractmethod
    def get_officer_by_badge(self, badge: str) -> Optional[OfficerEntity]:
        raise NotImplementedError()

    @abstractmethod
    def get_officer_by_id(self, id: str) -> Optional[OfficerEntity]:
        raise NotImplementedError()

    @abstractmethod
    def create_officer(self, officer: OfficerEntity) -> OfficerEntity:
        raise NotImplementedError()

    @abstractmethod
    def update_officer(self, id: str, officer: OfficerEntity) -> OfficerEntity:
        raise NotImplementedError()

    @abstractmethod
    def delete_officer(self, id: str) -> None:
        raise NotImplementedError()
