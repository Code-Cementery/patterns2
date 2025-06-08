from ..base import Base
from ..ctx import get_engine


def schema_exists():
    with get_engine() as engine:
        with engine.begin() as conn:
            return conn.execute(f"""SELECT EXISTS(
                SELECT 1
                FROM information_schema.schemata
                WHERE schema_name = '{Base.metadata.schema}'
            )""").scalar()
