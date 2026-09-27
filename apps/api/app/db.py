"""Database engine + session management (SQLAlchemy 2.0, async)."""
from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# TODO(M1): create the async engine and an `async_sessionmaker` from settings.database_url.


async def get_session() -> AsyncIterator[AsyncSession]:
    """TODO(M1): FastAPI dependency yielding one session per request.

    Commit on success, roll back on exception, always close.
    """
    raise NotImplementedError
    yield  # pragma: no cover  (keeps this a generator for type checkers)
