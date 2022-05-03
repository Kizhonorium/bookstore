from enum import Enum

from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR, ENUM


class MysqlRoleMixin:
    class RoleStatus(Enum):
        admin = "admin"
        user = "user"

    role = Column(
        "role",
        ENUM(RoleStatus),
        index=True,
        unique=False,
        nullable=False,
        server_default=str(RoleStatus.user.value),
    )
