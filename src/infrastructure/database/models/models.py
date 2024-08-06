import enum

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.domain import InfractionEntity, OfficerEntity, PersonEntity, VehicleEntity
from src.infrastructure.database.config import Base


class RoleEnum(enum.Enum):
    ADMIN = "ADMIN"
    OFFICER = "OFFICER"


class PersonModel(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    vehicles = relationship(
        "VehicleModel", back_populates="owner", cascade="all, delete-orphan"
    )

    def to_entity(self) -> PersonEntity:
        return PersonEntity(
            id=self.id,
            name=self.name,
            email=self.email,
        )

    @staticmethod
    def from_entity(person: PersonEntity) -> "PersonModel":
        return PersonModel(
            id=person.id,
            name=person.name,
            email=person.email,
        )


class VehicleModel(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    license_plate = Column(String, unique=True, index=True)
    brand = Column(String, index=True)
    color = Column(String, index=True)
    owner_id = Column(
        Integer, ForeignKey("people.id", ondelete="CASCADE"), nullable=False
    )

    owner = relationship("PersonModel", back_populates="vehicles")
    infractions = relationship(
        "InfractionModel", back_populates="vehicle", cascade="all, delete-orphan"
    )

    def to_entity(self) -> VehicleEntity:
        return VehicleEntity(
            id=self.id,
            license_plate=self.license_plate,
            brand=self.brand,
            color=self.color,
            owner_id=self.owner_id,
        )

    @staticmethod
    def from_entity(vehicle: VehicleEntity) -> "VehicleModel":
        return VehicleModel(
            id=vehicle.id,
            license_plate=vehicle.license_plate,
            brand=vehicle.brand,
            color=vehicle.color,
            owner_id=vehicle.owner_id,
        )


class OfficerModel(Base):
    __tablename__ = "officers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    badge_number = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(Enum(RoleEnum), default=RoleEnum.OFFICER)

    def to_entity(self) -> OfficerEntity:
        return OfficerEntity(
            id=self.id,
            name=self.name,
            badge_number=self.badge_number,
            hashed_password=self.hashed_password,
            role=self.role.value,
        )

    @staticmethod
    def from_entity(officer: OfficerEntity) -> "OfficerModel":
        return OfficerModel(
            name=officer.name,
            badge_number=officer.badge_number,
            hashed_password=officer.hashed_password,
            role=RoleEnum(officer.role) if officer.role else RoleEnum.OFFICER,
        )


class InfractionModel(Base):
    __tablename__ = "infractions"

    id = Column(Integer, primary_key=True, index=True)
    license_plate = Column(
        String, ForeignKey("vehicles.license_plate"), index=True, nullable=False
    )
    timestamp = Column(DateTime)
    comments = Column(String)

    vehicle = relationship("VehicleModel", back_populates="infractions")

    def to_entity(self) -> InfractionEntity:
        vehicle_entity = self.vehicle.to_entity() if self.vehicle else None
        return InfractionEntity(
            id=self.id,
            license_plate=self.license_plate,
            timestamp=self.timestamp,
            comments=self.comments,
            vehicle=vehicle_entity,
        )

    @staticmethod
    def from_entity(infraction: InfractionEntity) -> "InfractionModel":
        return InfractionModel(
            id=infraction.id,
            license_plate=infraction.license_plate,
            timestamp=infraction.timestamp,
            comments=infraction.comments,
        )
