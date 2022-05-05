from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT

from database.models.base import Base
from database.models.mixins import MysqlPrimaryKeyMixin, MysqlTimestampsMixin


class BookCategory(Base, MysqlPrimaryKeyMixin, MysqlTimestampsMixin):
    __tablename__ = "books_categories"

    category_id = Column(BIGINT(unsigned=True), index=True, nullable=False, unique=True)
    book_id = Column(BIGINT(unsigned=True), index=True, nullable=False, unique=True)
