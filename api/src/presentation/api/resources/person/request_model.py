from pydantic import BaseModel


class PersonBaseModel(BaseModel):
    name: str
    email: str


class PersonCreate(PersonBaseModel):
    pass


class PersonUpdate(BaseModel):
    name: str
