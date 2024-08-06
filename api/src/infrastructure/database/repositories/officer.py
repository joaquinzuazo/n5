from typing import Optional

from sqlalchemy.orm import Session
from src.domain import OfficerEntity, OfficerRepository
from src.infrastructure.database.models import OfficerModel


class OfficerRepositoryImpl(OfficerRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_officer_by_badge(self, badge: str) -> Optional[OfficerEntity]:
        officer = (
            self.session.query(OfficerModel)
            .filter(OfficerModel.badge_number == badge)
            .first()
        )
        if not officer:
            return None
        return officer.to_entity()

    def get_officer_by_id(self, id: str) -> Optional[OfficerEntity]:
        officer = self.session.query(OfficerModel).filter(OfficerModel.id == id).first()
        if not officer:
            return None
        return officer.to_entity()

    def create_officer(self, officer: OfficerEntity) -> OfficerEntity:
        officer_model = OfficerModel.from_entity(officer)
        self.session.add(officer_model)
        self.session.commit()
        return officer_model.to_entity()

    def update_officer(self, id: str, officer: OfficerEntity) -> OfficerEntity:
        officer_model = (
            self.session.query(OfficerModel).filter(OfficerModel.id == id).first()
        )
        officer_model.name = officer.name
        officer_model.badge_number = officer.badge_number
        self.session.commit()
        return officer_model.to_entity()

    def delete_officer(self, id: str) -> None:
        officer = self.session.query(OfficerModel).filter(OfficerModel.id == id).first()
        self.session.delete(officer)
        self.session.commit()
