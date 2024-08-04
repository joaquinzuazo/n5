from abc import ABC, abstractmethod
from typing import List

from src.domain import InfractionEntity


class InfractionRepository(ABC):
    @abstractmethod
    def get_infractions_by_user_id(self, user_id: int) -> List[InfractionEntity]:
        raise NotImplementedError()

    @abstractmethod
    def create_infraction(self, infraction: InfractionEntity) -> None:
        raise NotImplementedError()
