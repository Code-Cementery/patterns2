from sqlalchemy.engine import URL, Engine, create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine as aio_create_async_engine
from sqlalchemy.orm import Session, sessionmaker

from app.cfg import get_db_cfg, DatabaseSettings

DB_AIO = False

_settings: DatabaseSettings = get_db_cfg()

_engine = aio_create_async_engine(_settings.url) if DB_AIO else create_engine(_settings.url)


class EngineContext:
    def __init__(self, engine):
        self.engine = engine

    def __enter__(self) -> Engine:
        return self.engine

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.engine.dispose()

_session_factory = sessionmaker(
    bind=_engine,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
    class_=Session,
)


def get_engine() -> EngineContext:
    return EngineContext(_engine)


def get_session() -> sessionmaker:
    return _session_factory.begin()
