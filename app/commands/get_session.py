from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from utils import mysql_connection_string


engine = create_engine(mysql_connection_string())
session = Session(engine)