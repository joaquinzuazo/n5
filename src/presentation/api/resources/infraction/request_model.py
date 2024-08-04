from datetime import datetime

from pydantic import BaseModel


class InfractionCreateRequest(BaseModel):
    license_plate: str
    timestamp: datetime
    comments: str
