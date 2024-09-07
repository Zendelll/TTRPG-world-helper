from pydantic import BaseModel
from typing import Optional, List, Union

class EntityBase(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    parent_id: Optional[str] = None
    children: List[Union["Place", "Character", "Event", "Folder", "Item"]] = []

    class Config:
        orm_mode = True

class Place(EntityBase):
    map_path: Optional[str] = None
    image_path: Optional[str] = None
    coordinates: Optional[List[dict]] = None

class Character(EntityBase):
    image_path: Optional[str] = None

class Event(EntityBase):
    image_path: Optional[str] = None

class Item(EntityBase):
    image_path: Optional[str] = None

class Folder(EntityBase):
    pass



class EntityCreate(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    parent_id: Optional[str] = None

class PlaceCreate(EntityCreate):
    map_path: Optional[str] = None
    image_path: Optional[str] = None
    coordinates: Optional[str] = None

class CharacterCreate(EntityCreate):
    image_path: Optional[str] = None

class EventCreate(EntityCreate):
    image_path: Optional[str] = None

class ItemCreate(EntityCreate):
    image_path: Optional[str] = None

class FolderCreate(EntityCreate):
    pass
