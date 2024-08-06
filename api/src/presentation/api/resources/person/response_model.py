from pydantic import BaseModel


class PersonReadModel(BaseModel):
    id: int
    name: str
    email: str
