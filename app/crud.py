from sqlalchemy.orm import Session
from typing import List, Optional

from . import models, schemas

def create_item(db: Session, item_in: schemas.ItemCreate) -> models.Item:
    db_item = models.Item(name=item_in.name, description=item_in.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_item(db: Session, item_id: int) -> Optional[models.Item]:
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_items(db: Session) -> List[models.Item]:
    return db.query(models.Item).order_by(models.Item.id).all()
