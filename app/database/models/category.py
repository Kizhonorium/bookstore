from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR, BIGINT, TEXT

from database.models.base import Base
from database.models.mixins import MysqlPrimaryKeyMixin, MysqlTimestampsMixin


class Category(Base, MysqlPrimaryKeyMixin, MysqlTimestampsMixin):
    __tablename__ = "categories"

    name = Column(VARCHAR(128), nullable=False, index=True, unique=True)
    description = Column(TEXT(), nullable=True, index=False, unique=False)
    parent_id = Column(BIGINT(unsigned=True), index=True, nullable=True, unique=True)
