from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, DATE

from database.models.base import Base
from database.models.mixins import MysqlPrimaryKeyMixin, MysqlTimestampsMixin


class BookPublishingHouse(Base, MysqlPrimaryKeyMixin, MysqlTimestampsMixin):
    __tablename__ = "books_publishing_houses"

    publishing_house_id = Column(BIGINT(unsigned=True), index=True, nullable=False, unique=True)
    book_id = Column(BIGINT(unsigned=True), index=True, nullable=False, unique=True)
    publishing_year = Column(DATE(), nullable=False, index=True, unique=True)
