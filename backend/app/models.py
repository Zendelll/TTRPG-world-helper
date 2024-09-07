from sqlalchemy import Column, String, Text, ForeignKey, Enum, JSON, UniqueConstraint, Integer
from sqlalchemy.orm import relationship
from app.db import Base
import enum

class EntityType(enum.Enum):
    PLACE = "place"
    CHARACTER = "character"
    EVENT = "event"
    FOLDER = "folder"
    ITEM = "item"

class Entity(Base):
    __tablename__ = "entities"

    id = Column(String, index=True, primary_key=True)
    parent_id = Column(String, ForeignKey("entities.id"), nullable=True)
    entity_type = Column(Enum(EntityType), nullable=False)
    name = Column(String, index=True)
    description = Column(Text, nullable=True)
    
    parent = relationship("Entity", back_populates="children", remote_side=[id])
    children = relationship("Entity", back_populates="parent")

    image_path = Column(String, nullable=True)
    
    __table_args__ = (
        UniqueConstraint('parent_id', 'id', name='uq_parent_id_id'),
    )

    __mapper_args__ = {
        'polymorphic_identity': 'entity',
        'polymorphic_on': entity_type
    }

class Place(Entity):
    __mapper_args__ = {'polymorphic_identity': EntityType.PLACE}
    map_path = Column(String, nullable=True)
    coordinates = Column(JSON, nullable=True)

class Character(Entity):
    __mapper_args__ = {'polymorphic_identity': EntityType.CHARACTER}

class Event(Entity):
    __mapper_args__ = {'polymorphic_identity': EntityType.EVENT}

class Folder(Entity):
    __mapper_args__ = {'polymorphic_identity': EntityType.FOLDER}

class Item(Entity):
    __mapper_args__ = {'polymorphic_identity': EntityType.ITEM}
