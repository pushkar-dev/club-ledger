from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    count: int


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    club_id: int

    class Config:
        orm_mode = True
