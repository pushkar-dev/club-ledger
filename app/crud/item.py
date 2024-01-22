from sqlalchemy.orm import Session

from app.models import Item
from app.schemas.item import ItemCreate


def create_item(db: Session, item: ItemCreate, club_id: int):
    db_item = Item(**item.dict(), club_id=club_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()
