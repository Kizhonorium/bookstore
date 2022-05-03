from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR, TEXT, BIGINT

from database.models.base import Base
from database.models.mixins import MysqlPrimaryKeyMixin, MysqlTimestampsMixin


class SubCategory(Base, MysqlPrimaryKeyMixin, MysqlTimestampsMixin):
    __tablename__ = "subcategories"

    category_id = Column(BIGINT(unsigned=True), index=True, nullable=False, unique=True)
    name = Column(VARCHAR(128), nullable=False, index=True, unique=True)
    description = Column(TEXT(), nullable=True, index=False, unique=False)
