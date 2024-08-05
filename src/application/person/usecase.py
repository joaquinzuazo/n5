from abc import ABC, abstractmethod
from typing import Optional

from src.domain import PersonEntity, PersonExists, PersonIDNotFound
from src.presentation.api.resources.person.request_model import (
    PersonCreate,
    PersonUpdate,
)


class PersonUseCase(ABC):
    @abstractmethod
    def get_person_by_email(self, email: str) -> Optional[PersonEntity]:
        raise NotImplementedError()

    def get_person_by_id(self, id: str) -> Optional[PersonEntity]:
        raise NotImplementedError()

    def get_persons(self) -> list[PersonEntity]:
        raise NotImplementedError()

    @abstractmethod
    def create_person(self, person: PersonCreate) -> None:
        raise NotImplementedError()

    @abstractmethod
    def update_person(self, id: str, email: str, update_person: PersonUpdate) -> None:
        raise NotImplementedError()

    @abstractmethod
    def delete_person(self, id: str, email: str) -> None:
        raise NotImplementedError()


class PersonUseCaseImpl(PersonUseCase):
    def __init__(self, person_repository):
        self.person_repository = person_repository

    def get_person_by_email(self, email: str) -> Optional[PersonEntity]:
        try:
            return self.person_repository.get_person_by_email(email)
        except Exception as e:
            raise e

    def get_person_by_id(self, id: str) -> Optional[PersonEntity]:
        try:
            return self.person_repository.get_person_by_id(id)
        except Exception as e:
            raise e

    def get_persons(self) -> list[PersonEntity]:
        try:
            return self.person_repository.get_persons()
        except Exception as e:
            raise e

    def create_person(self, person: PersonCreate) -> None:
        try:
            person_exists = self.person_repository.get_person_by_email(person.email)
            if person_exists:
                raise PersonExists

            person = PersonEntity(
                id=None,
                name=person.name,
                email=person.email,
            )

            self.person_repository.create_person(person)
        except Exception as e:
            raise e

    def update_person(self, id: int, person_update: PersonUpdate) -> None:
        try:
            person = self.person_repository.get_person_by_id(id)
            if not person:
                raise PersonIDNotFound

            person_update = PersonEntity(
                id=id,
                name=person_update.name,
                email=person.email,
            )

            self.person_repository.update_person(person_update)
        except Exception as e:
            raise e

    def delete_person(self, id: str) -> None:
        try:
            person = self.person_repository.get_person_by_id(id)
            if not person:
                raise PersonIDNotFound
            self.person_repository.delete_person(id)
        except Exception as e:
            raise e
