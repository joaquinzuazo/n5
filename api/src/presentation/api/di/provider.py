from typing import Generator

from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from src.application.infraction.usecase import InfractionUseCase, InfractionUseCaseImpl
from src.application.officer.usecase import OfficerUseCase, OfficerUseCaseImpl
from src.application.person.usecase import PersonUseCase, PersonUseCaseImpl
from src.application.vehicle.usecase import VehicleUseCase, VehicleUseCaseImpl
from src.infrastructure.database.config import SessionLocal
from src.infrastructure.database.repositories.infraction import InfractionRepositoryImpl
from src.infrastructure.database.repositories.officer import OfficerRepositoryImpl
from src.infrastructure.database.repositories.person import PersonRepositoryImpl
from src.infrastructure.database.repositories.vehicle import VehicleRepositoryImpl
from src.utils.jwt import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db() -> Generator[Session, None, None]:
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


def officer_usecase(db: Session = Depends(get_db)) -> OfficerUseCase:
    officer_repository = OfficerRepositoryImpl(db)
    return OfficerUseCaseImpl(officer_repository)


def person_usecase(db: Session = Depends(get_db)) -> PersonUseCase:
    person_repository = PersonRepositoryImpl(db)
    return PersonUseCaseImpl(person_repository)


def vehicle_usecase(db: Session = Depends(get_db)) -> VehicleUseCase:
    vehicle_repository = VehicleRepositoryImpl(db)
    person_repository = PersonRepositoryImpl(db)
    return VehicleUseCaseImpl(vehicle_repository, person_repository)


def get_token_payload(token: str = Depends(oauth2_scheme)):
    try:
        valid_token = verify_token(token)
        if not valid_token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired"
            )

        return valid_token
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )


def get_current_officer(
    token: dict = Depends(get_token_payload),
    officer_usecase: OfficerUseCase = Depends(officer_usecase),
):
    try:
        badge = token.get("badge")
        officer = officer_usecase.get_officer_by_badge(badge)
        return officer
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
