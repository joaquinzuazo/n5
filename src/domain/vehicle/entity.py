from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from src.domain.infraction.entity import Infraction as InfractionEntity
    from src.domain.person.entity import PersonEntity


class VehicleEntity:
    def __init__(
        self,
        id: Optional[int],
        license_plate: str,
        brand: str,
        color: str,
        owner: Optional["PersonEntity"] = None,
    ):
        self.id = id
        self.license_plate = license_plate
        self.brand = brand
        self.color = color
        self.owner = owner
