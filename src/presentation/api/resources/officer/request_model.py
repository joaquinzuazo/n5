from pydantic import BaseModel


class OfficerBase(BaseModel):
    badge_number: str


class OfficerLogin(OfficerBase):
    badge_number: str
    password: str


class OfficerCreate(OfficerBase):
    name: str
    password: str
    role: str


class OfficerUpdate(OfficerBase):
    name: str
