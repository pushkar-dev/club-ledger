from pydantic import BaseModel


class ClubBase(BaseModel):
    name: str


class ClubCreate(ClubBase):
    pass


class Club(ClubBase):
    id: int

    class Config:
        orm_mode = True
