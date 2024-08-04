from fastapi import Depends, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from src.application.infraction.usecase import InfractionUseCase, InfractionUseCaseImpl
from src.application.officer.usecase import OfficerUseCase, OfficerUseCaseImpl
from src.infrastructure.database.config import SessionLocal
from src.infrastructure.database.repositories.infraction import InfractionRepositoryImpl
from src.infrastructure.database.repositories.officer import OfficerRepositoryImpl
from src.infrastructure.database.repositories.person import PersonRepositoryImpl
from src.infrastructure.database.repositories.vehicle import VehicleRepositoryImpl
from src.presentation.api.resources.commons.response_model import ResponseModel
from src.utils.jwt import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


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


def validate_token(token: str = Depends(oauth2_scheme)):
    if not token:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content=ResponseModel(
                error=True, message="Token not provided", data={}
            ).dict(),
        )
    try:
        verify_token(token)
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=ResponseModel(error=True, message="Invalid token", data={}).dict(),
        )
