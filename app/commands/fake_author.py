from faker import Faker

from sqlalchemy import insert
from sqlalchemy.orm import Session

from utils import sql_execute
from .get_session import session
from database.models import Author


fake = Faker()


def fake_author(count_authors: int = 1, transaction: Session = session):
    for iteration in range(count_authors):
        first_name, last_name = None, None

        try:
            first_name, last_name = fake.name().split()
        except ValueError as err:
            return fake_author(count_authors - iteration)

        author = {
            "first_name": first_name,
            "last_name": last_name,
            "email": fake.email(),
            "country": fake.country(),
            "date_birth": fake.date(),
        }
        insert_author(author, transaction)


def insert_author(author: dict, transaction: Session):
    stmt = insert(Author).values(author)
    sql_execute(transaction, stmt)
