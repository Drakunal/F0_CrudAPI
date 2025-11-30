from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, crud
from ..session import SessionLocal

router = APIRouter(prefix="/items", tags=["items"])

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ItemRead, status_code=status.HTTP_201_CREATED)
def create_item(item_in: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item_in)

@router.get("/", response_model=List[schemas.ItemRead])
def read_items(db: Session = Depends(get_db)):
    return crud.get_items(db)

@router.get("/{item_id}", response_model=schemas.ItemRead)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put("/{item_id}", response_model=schemas.ItemRead)
def update_item(item_id: int, item_in: schemas.ItemUpdate, db: Session = Depends(get_db)):
    db_item = crud.update_item(db, item_id, item_in)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_item(db, item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return None

