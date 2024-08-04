from pydantic import BaseModel


class OfficierLogin(BaseModel):
    badge_number: str
    password: str
