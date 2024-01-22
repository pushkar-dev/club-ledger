from fastapi import FastAPI
from app.routers import user, club, item
from app.db.session import Base, engine

app = FastAPI()

app.include_router(user.router)
app.include_router(club.router)
app.include_router(item.router)
