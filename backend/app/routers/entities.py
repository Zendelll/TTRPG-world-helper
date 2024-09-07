import re
import json
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, Form
from sqlalchemy.orm import Session
from typing import Union, Optional
from app import crud, schemas
from app.db import get_db
import os
import shutil

router = APIRouter()

ID_REGEX = re.compile(r'^[a-zA-Z0-9_]+(-[a-zA-Z0-9_]+)*$')

def save_file(file: UploadFile, file_path: str) -> str:
    """Helper function to save uploaded file to the server."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return file_path


@router.post("/place", response_model=schemas.Place)
async def create_place(
    id: str = Form(...),
    name: str = Form(...),
    description: Optional[str] = Form(None),
    parent_id: Optional[str] = Form(None),
    coordinates: Optional[str] = Form(None),
    map_file: Optional[UploadFile] = File(None),
    image_file: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    full_id = f"{parent_id}-{id}" if parent_id else id
    if not ID_REGEX.match(full_id):
        raise HTTPException(status_code=400, detail="Invalid ID format")
    
    if coordinates:
        try:
            coordinates = json.loads(coordinates)
            if isinstance(coordinates, dict):
                coordinates = [coordinates]
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Invalid JSON format for coordinates")

    map_path, image_path = None, None
    if map_file:
        map_extension = os.path.splitext(map_file.filename)[1]
        map_path = save_file(map_file, f"uploads/maps/{full_id}{map_extension}")
    if image_file:
        image_extension = os.path.splitext(image_file.filename)[1]
        image_path = save_file(image_file, f"uploads/images/{full_id}{image_extension}")

    if parent_id:
        parent_entity = crud.get_entity(db, parent_id)
        if not parent_entity:
            raise HTTPException(status_code=404, detail="Parent entity not found")

        existing_child = crud.get_entity(db, f"{parent_id}-{id}")
        if existing_child:
            raise HTTPException(status_code=400, detail="A child with this ID already exists under the specified parent")

    place = schemas.PlaceCreate(
        id=full_id,
        name=name,
        description=description,
        parent_id=parent_id,
        map_path=map_path,
        image_path=image_path,
        coordinates = coordinates
    )
    return crud.create_place(db, place)

@router.post("/character", response_model=schemas.Character)
async def create_character(
    id: str = Form(...),
    name: str = Form(...),
    description: Optional[str] = Form(None),
    parent_id: Optional[str] = Form(None),
    image_file: Optional[UploadFile] = File(None),  # Optional image file
    db: Session = Depends(get_db)
):
    full_id = f"{parent_id}-{id}" if parent_id else id
    if not ID_REGEX.match(full_id):
        raise HTTPException(status_code=400, detail="Invalid ID format")
    
    image_path = None
    if image_file:
        image_extension = os.path.splitext(image_file.filename)[1]
        image_path = save_file(image_file, f"uploads/images/{full_id}{image_extension}")

    if parent_id:
        parent_entity = crud.get_entity(db, parent_id)
        if not parent_entity:
            raise HTTPException(status_code=404, detail="Parent entity not found")

        existing_child = crud.get_entity(db, f"{parent_id}-{id}")
        if existing_child:
            raise HTTPException(status_code=400, detail="A child with this ID already exists under the specified parent")

    character = schemas.CharacterCreate(
        id=full_id,
        name=name,
        description=description,
        parent_id=parent_id,
        image_path=image_path
    )
    return crud.create_character(db, character)

@router.post("/event", response_model=schemas.Event)
async def create_event(
    id: str = Form(...),
    name: str = Form(...),
    description: Optional[str] = Form(None),
    parent_id: Optional[str] = Form(None),
    image_file: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    full_id = f"{parent_id}-{id}" if parent_id else id
    if not ID_REGEX.match(full_id):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    image_path = None
    if image_file:
        image_extension = os.path.splitext(image_file.filename)[1]
        image_path = save_file(image_file, f"uploads/images/{full_id}{image_extension}")

    if parent_id:
        parent_entity = crud.get_entity(db, parent_id)
        if not parent_entity:
            raise HTTPException(status_code=404, detail="Parent entity not found")

        existing_child = crud.get_entity(db, f"{parent_id}-{id}")
        if existing_child:
            raise HTTPException(status_code=400, detail="A child with this ID already exists under the specified parent")

    event = schemas.EventCreate(
        id=full_id,
        name=name,
        description=description,
        parent_id=parent_id,
        image_path=image_path
    )
    return crud.create_event(db, event)

@router.post("/item", response_model=schemas.Item)
async def create_item(
    id: str = Form(...),
    name: str = Form(...),
    description: Optional[str] = Form(None),
    parent_id: Optional[str] = Form(None),
    image_file: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    full_id = f"{parent_id}-{id}" if parent_id else id
    if not ID_REGEX.match(full_id):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    image_path = None
    if image_file:
        image_extension = os.path.splitext(image_file.filename)[1]
        image_path = save_file(image_file, f"uploads/images/{full_id}{image_extension}")

    if parent_id:
        parent_entity = crud.get_entity(db, parent_id)
        if not parent_entity:
            raise HTTPException(status_code=404, detail="Parent entity not found")

        existing_child = crud.get_entity(db, f"{parent_id}-{id}")
        if existing_child:
            raise HTTPException(status_code=400, detail="A child with this ID already exists under the specified parent")

    item = schemas.ItemCreate(
        id=full_id,
        name=name,
        description=description,
        parent_id=parent_id,
        image_path=image_path
    )
    return crud.create_item(db, item)

@router.post("/folder", response_model=schemas.Folder)
def create_folder(folder: schemas.FolderCreate, db: Session = Depends(get_db)):

    full_id = f"{folder.parent_id}-{folder.id}" if folder.parent_id else folder.id
    if not ID_REGEX.match(full_id):
        raise HTTPException(status_code=400, detail="Invalid ID format")
    folder.id = full_id
    
    if folder.parent_id:
        parent_entity = crud.get_entity(db, folder.parent_id)
        if not parent_entity:
            raise HTTPException(status_code=404, detail="Parent entity not found")
        
        existing_child = crud.get_entity(db, f"{folder.parent_id}-{folder.id}")
        if existing_child:
            raise HTTPException(status_code=400, detail="A child with this ID already exists under the specified parent")
    
    return crud.create_folder(db, folder)


@router.get("/{entity_id}", response_model=Union[schemas.Place, schemas.Character, schemas.Event, schemas.Folder, schemas.Item])
def read_entity(entity_id: str, db: Session = Depends(get_db)):
    if not ID_REGEX.match(entity_id):
        raise HTTPException(status_code=400, detail="Invalid entity ID format")

    db_entity = crud.get_entity(db, entity_id)
    if not db_entity:
        raise HTTPException(status_code=404, detail="Entity not found")

    return db_entity

@router.get("/check/{entity_id}", response_model=bool)
def read_entity(entity_id: str, db: Session = Depends(get_db)):
    if not ID_REGEX.match(entity_id):
        raise HTTPException(status_code=400, detail="Invalid entity ID format")
    return bool(crud.get_entity(db, entity_id))
