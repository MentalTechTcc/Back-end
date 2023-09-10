from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings
from unittest.mock import Mock
from os import getenv


SQLALCHEMY_DATABASE_URL = settings.db_connect_url
print("db_url" , SQLALCHEMY_DATABASE_URL)
if not getenv("TEST"):
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL
    )
else:
    print("Em modo de teste !")
    engine = Mock() 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        raise e
    finally:
        db.close()
    return db

def createTables():
    Base.metadata.create_all(bind=engine) 