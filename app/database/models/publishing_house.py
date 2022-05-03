from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR, TEXT

from database.models.base import Base
from database.models.mixins import MysqlPrimaryKeyMixin, MysqlTimestampsMixin


class PublishingHouse(Base, MysqlPrimaryKeyMixin, MysqlTimestampsMixin):
    __tablename__ = "publishing_houses"

    name = Column(VARCHAR(128), nullable=False, index=True, unique=True)
    country = Column(VARCHAR(255), nullable=False, index=True, unique=False)
    city = Column(VARCHAR(255), nullable=False, index=False, unique=False)
    state = Column(VARCHAR(255), nullable=False, index=False, unique=False)
    postal_code = Column(VARCHAR(255), nullable=False, index=False, unique=False)
    street = Column(VARCHAR(255), nullable=False, index=False, unique=False)
    headquarters_number = Column(VARCHAR(255), nullable=False, index=False, unique=False)
    description = Column(TEXT(), nullable=True, index=False, unique=False)
