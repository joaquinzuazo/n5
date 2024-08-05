from typing import Optional

from sqlalchemy.orm import Session

from src.domain import PersonEntity, PersonRepository
from src.infrastructure.database.models import PersonModel


class PersonRepositoryImpl(PersonRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_person_by_email(self, email: str) -> Optional[PersonEntity]:
        person = (
            self.session.query(PersonModel).filter(PersonModel.email == email).first()
        )
        if not person:
            return None
        return person.to_entity()

    def create_person(self, person: PersonEntity) -> PersonEntity:
        person_model = PersonModel.from_entity(person)
        self.session.add(person_model)
        self.session.commit()
        return person_model.to_entity()

    def update_person(self, person: PersonEntity) -> PersonEntity:
        person_model = (
            self.session.query(PersonModel).filter(PersonModel.id == person.id).first()
        )
        person_model.name = person.name
        person_model.email = person.email
        self.session.commit()
        return person_model.to_entity()

    def delete_person(self, id: str) -> None:
        person = self.session.query(PersonModel).filter(PersonModel.id == id).first()
        self.session.delete(person)
        self.session.commit()

    def get_persons(self) -> list[PersonEntity]:
        return [person.to_entity() for person in self.session.query(PersonModel).all()]
