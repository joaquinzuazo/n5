from pydantic import BaseModel
from src.infrastructure.database.models.models import RoleEnum


class OfficerBase(BaseModel):
    badge_number: str


class OfficerLogin(OfficerBase):
    badge_number: str
    password: str


class OfficerCreate(OfficerBase):
    name: str
    password: str
    role: RoleEnum


class OfficerUpdate(OfficerBase):
    name: str
