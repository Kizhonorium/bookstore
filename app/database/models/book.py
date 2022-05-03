from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR

from database.models.base import Base
from database.models.mixins import MysqlPrimaryKeyMixin, MysqlTimestampsMixin


class Book(Base, MysqlPrimaryKeyMixin, MysqlTimestampsMixin):
    __tablename__ = "books"

    name = Column(VARCHAR(128), nullable=False, index=True, unique=True)
    price = Column(VARCHAR(10), nullable=False, index=True, unique=False)
    currency = Column(VARCHAR(10), nullable=False, index=False, unique=False)
