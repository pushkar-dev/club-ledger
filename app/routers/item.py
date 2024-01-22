from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db.base import get_db

router = APIRouter()


@router.post("/clubs/{club_id}/items/", response_model=schemas.Item)
def create_item(club_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item, club_id=club_id)


@router.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
