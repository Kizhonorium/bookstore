from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from utils import mysql_connection_string


engine = create_engine(mysql_connection_string())
session = Session(engine)


def get_db() -> Generator:
    db = session
    try:
        yield db
    finally:
        db.close()
