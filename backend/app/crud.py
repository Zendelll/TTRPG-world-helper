from sqlalchemy.orm import Session
from app import models, schemas

#TODO: Set relationship with parent
def create_place(db: Session, place: schemas.PlaceCreate):
    db_place = models.Place(
        **place.model_dump(),
        entity_type = models.EntityType.PLACE
    )
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place

def create_character(db: Session, character: schemas.CharacterCreate):
    db_character = models.Character(
        **character.model_dump(),
        entity_type = models.EntityType.CHARACTER
    )
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character

def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(
        **event.model_dump(),
        entity_type = models.EntityType.EVENT
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def create_folder(db: Session, folder: schemas.FolderCreate):
    db_folder = models.Folder(
        **folder.model_dump(),
        entity_type = models.EntityType.FOLDER
    )
    db.add(db_folder)
    db.commit()
    db.refresh(db_folder)
    return db_folder

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(
        **item.model_dump(),
        entity_type = models.EntityType.ITEM
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_entity(db: Session, full_entity_id: str):
    return db.query(models.Entity).filter(
        models.Entity.id == full_entity_id
    ).first()

