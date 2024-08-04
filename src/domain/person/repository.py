from abc import ABC, abstractmethod
from typing import Optional

from src.domain import PersonEntity


class PersonRepository(ABC):
    @abstractmethod
    def get_person_by_email(self, email: str) -> Optional[PersonEntity]:
        raise NotImplementedError()
