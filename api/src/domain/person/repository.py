from abc import ABC, abstractmethod
from typing import Optional

from src.domain import PersonEntity


class PersonRepository(ABC):
    @abstractmethod
    def get_person_by_email(self, email: str) -> Optional[PersonEntity]:
        raise NotImplementedError()

    @abstractmethod
    def get_persons(self) -> list[PersonEntity]:
        raise NotImplementedError()

    @abstractmethod
    def get_person_by_id(self, id: str) -> Optional[PersonEntity]:
        raise NotImplementedError()

    @abstractmethod
    def create_person(self, person: PersonEntity) -> PersonEntity:
        raise NotImplementedError()

    @abstractmethod
    def update_person(self, person: PersonEntity) -> PersonEntity:
        raise NotImplementedError()

    @abstractmethod
    def delete_person(self, id: str) -> None:
        raise NotImplementedError()
