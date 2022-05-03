from sqlalchemy import Column
from sqlalchemy.orm import validates
from sqlalchemy.dialects.mysql import VARCHAR, TEXT, BOOLEAN
from sqlalchemy.sql.expression import true

from database.models.base import Base
from database.models.mixins import MysqlPrimaryKeyMixin, MysqlTimestampsMixin, MysqlRoleMixin


class User(Base, MysqlPrimaryKeyMixin, MysqlTimestampsMixin, MysqlRoleMixin):
    __tablename__ = "users"

    first_name = Column(VARCHAR(128), nullable=False, index=True, unique=False)
    last_name = Column(VARCHAR(128), nullable=False, index=True, unique=False)
    phone = Column(VARCHAR(15), nullable=False, index=False, unique=False)
    email = Column(VARCHAR(128), nullable=False, index=False, unique=True)
    hashed_password = Column(TEXT(), nullable=False, unique=False)
    is_active = Column(BOOLEAN(), nullable=False, server_default=true())

    @validates("email")
    def validate_email(self, key, address):
        if any([_ not in address for _ in ("@", ".com")]):
            raise ValueError("Failed, in email must be <@> and <.com>")
        return address
