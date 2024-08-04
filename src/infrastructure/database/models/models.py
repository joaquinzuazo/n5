from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.domain import InfractionEntity, PersonEntity, VehicleEntity
from src.infrastructure.database.config import Base


class PersonModel(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    vehicles = relationship("VehicleModel", back_populates="owner")

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
    owner_id = Column(Integer, ForeignKey("people.id"))

    owner = relationship("PersonModel", back_populates="vehicles")
    infractions = relationship("InfractionModel", back_populates="vehicle")

    def to_entity(self) -> VehicleEntity:
        return VehicleEntity(
            id=self.id,
            license_plate=self.license_plate,
            brand=self.brand,
            color=self.color,
            owner=self.owner.to_entity() if self.owner else None,
        )

    @staticmethod
    def from_entity(vehicle: VehicleEntity) -> "VehicleModel":
        return VehicleModel(
            id=vehicle.id,
            license_plate=vehicle.license_plate,
            brand=vehicle.brand,
            color=vehicle.color,
            owner=PersonModel.from_entity(vehicle.owner) if vehicle.owner else None,
        )


class OfficerModel(Base):
    __tablename__ = "officers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    badge_number = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class InfractionModel(Base):
    __tablename__ = "infractions"

    id = Column(Integer, primary_key=True, index=True)
    license_plate = Column(String, ForeignKey("vehicles.license_plate"), index=True)
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
