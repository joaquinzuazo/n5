from typing import Generic, TypeVar

from pydantic import BaseModel

DataType = TypeVar("DataType")


class ResponseModel(BaseModel, Generic[DataType]):
    error: bool
    message: str
    data: list[DataType]
