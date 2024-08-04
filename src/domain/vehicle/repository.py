from abc import ABC, abstractmethod
from typing import Optional

from src.domain import VehicleEntity


class VehicleRepository(ABC):
    @abstractmethod
    def get_vehicle_by_license(self, license: str) -> Optional[VehicleEntity]:
        raise NotImplementedError()
