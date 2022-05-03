from sqlalchemy import Column
from sqlalchemy.orm import validates
from sqlalchemy.dialects.mysql import VARCHAR, DATE

from database.models.base import Base
from database.models.mixins import MysqlPrimaryKeyMixin, MysqlTimestampsMixin


class Author(Base, MysqlPrimaryKeyMixin, MysqlTimestampsMixin):
    __tablename__ = "authors"

    first_name = Column(VARCHAR(128), nullable=False, index=True, unique=False)
    last_name = Column(VARCHAR(128), nullable=False, index=True, unique=False)
    email = Column(VARCHAR(128), nullable=False, index=False, unique=True)
    country = Column(VARCHAR(255), nullable=False, index=True, unique=False)
    date_birth = Column(DATE(), nullable=False, index=True, unique=False)

    @validates("email")
    def validate_email(self, key, address):
        if any([_ not in address for _ in ("@", ".com")]):
            raise ValueError("Failed, in email must be <@> and <.com>")
        return address
