from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import getenv

SQLALCHEMY_DATABASE_URL = getenv('DATABASE_URL') #defined in production

if SQLALCHEMY_DATABASE_URL is None: # while migrating
    SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost:5432/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
