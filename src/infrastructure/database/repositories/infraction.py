from typing import List

from sqlalchemy.orm import Session

from src.domain import InfractionRepository
from src.domain.infraction.entity import InfractionEntity
from src.infrastructure.database.models import InfractionModel, VehicleModel


class InfractionRepositoryImpl(InfractionRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_infraction(self, infraction: InfractionEntity) -> None:
        db_infraction = InfractionModel.from_entity(infraction)
        self.db.add(db_infraction)
        self.db.commit()
        self.db.refresh(db_infraction)

    def get_infractions_by_user_id(self, user_id: int) -> List[InfractionEntity]:
        db_infractions = (
            self.db.query(InfractionModel)
            .join(VehicleModel)
            .filter(VehicleModel.owner_id == user_id)
            .all()
        )
        return [db_infraction.to_entity() for db_infraction in db_infractions]
