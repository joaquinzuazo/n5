from abc import ABC, abstractmethod
from typing import Optional

from src.domain import OfficerEntity


class OfficerRepository(ABC):
    @abstractmethod
    def get_officer_by_badge(self, badge: str) -> Optional[OfficerEntity]:
        raise NotImplementedError()
