from sqlalchemy.orm import Session

from app.models import Club
from app.schemas.club import ClubCreate


def create_club(db: Session, club: ClubCreate):
    db_club = Club(**club.dict())
    db.add(db_club)
    db.commit()
    db.refresh(db_club)
    return db_club


def get_club(db: Session, club_id: int):
    return db.query(Club).filter(Club.id == club_id).first()
