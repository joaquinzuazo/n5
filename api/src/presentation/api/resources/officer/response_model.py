from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    refresh_token: str


class OfficerRead(BaseModel):
    id: int
    name: str
    badge_number: str
    role: str
