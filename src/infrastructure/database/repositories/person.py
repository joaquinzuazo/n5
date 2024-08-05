from typing import Optional

from sqlalchemy.orm import Session

from src.domain import PersonEntity, PersonRepository
from src.infrastructure.database.models import PersonModel


class PersonRepositoryImpl(PersonRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_person_by_email(self, email: str) -> Optional[PersonEntity]:
        try:
            person = (
                self.session.query(PersonModel)
                .filter(PersonModel.email == email)
                .first()
            )
            if not person:
                return None
            return person.to_entity()
        except Exception as e:
            raise e

    def get_person_by_id(self, id: str) -> Optional[PersonEntity]:
        try:
            person = (
                self.session.query(PersonModel).filter(PersonModel.id == id).first()
            )
            if not person:
                return None
            return person.to_entity()
        except Exception as e:
            raise e

    def get_persons(self) -> list[PersonEntity]:
        try:
            return [
                person.to_entity() for person in self.session.query(PersonModel).all()
            ]
        except Exception as e:
            raise e

    def create_person(self, person: PersonEntity) -> PersonEntity:
        try:
            person_model = PersonModel.from_entity(person)
            self.session.add(person_model)
            self.session.commit()
            return person_model.to_entity()
        except Exception as e:
            raise e

    def update_person(self, person: PersonEntity) -> PersonEntity:
        try:
            person_model = (
                self.session.query(PersonModel)
                .filter(PersonModel.id == person.id)
                .first()
            )
            person_model.name = person.name
            self.session.commit()
            return person_model.to_entity()
        except Exception as e:
            raise e

    def delete_person(self, id: str) -> None:
        try:
            person = (
                self.session.query(PersonModel).filter(PersonModel.id == id).first()
            )
            self.session.delete(person)
            self.session.commit()
        except Exception as e:
            raise e
