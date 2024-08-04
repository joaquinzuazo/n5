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
