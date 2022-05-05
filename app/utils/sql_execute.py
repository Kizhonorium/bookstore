from typing import Union, Tuple

from sqlalchemy.orm import Session
from sqlalchemy.engine.cursor import CursorResult
from sqlalchemy.sql.base import Executable as SQLAlchemyExecutable


def sql_execute(transaction: Session, stmt: Union[SQLAlchemyExecutable, str]) -> CursorResult:
    if isinstance(stmt, SQLAlchemyExecutable):
        stmt_compiled = stmt.compile(compile_kwargs={"literal_binds": True})
        result = transaction.execute(str(stmt_compiled))
        transaction.commit()
    else:
        result = transaction.execute(stmt)
        transaction.commit()
    return result
