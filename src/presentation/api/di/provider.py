from fastapi import Depends
from sqlalchemy.orm import Session

from src.application.infraction.usecase import InfractionUseCase, InfractionUseCaseImpl
from src.application.officer.usecase import OfficerUseCase, OfficerUseCaseImpl
from src.infrastructure.database.config import SessionLocal
from src.infrastructure.database.repositories.infraction import InfractionRepositoryImpl
from src.infrastructure.database.repositories.officer import OfficerRepositoryImpl
from src.infrastructure.database.repositories.person import PersonRepositoryImpl
from src.infrastructure.database.repositories.vehicle import VehicleRepositoryImpl


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def infraction_usecase(db: Session = Depends(get_db)) -> InfractionUseCase:
    infraction_repository = InfractionRepositoryImpl(db)
    person_repository = PersonRepositoryImpl(db)
    vehicle_repository = VehicleRepositoryImpl(db)
    return InfractionUseCaseImpl(
        infraction_repository, person_repository, vehicle_repository
    )


def officer_login_usecase(db: Session = Depends(get_db)) -> OfficerUseCase:
    officer_repository = OfficerRepositoryImpl(db)
    return OfficerUseCaseImpl(officer_repository)
