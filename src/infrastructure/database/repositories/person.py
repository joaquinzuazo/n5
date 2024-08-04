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
