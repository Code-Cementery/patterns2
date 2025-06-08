import sys

from sqlalchemy import DDL

from .webapp import get_app
from .dal.base import Base as DeclarativeBase
from .dal import seeding, get_engine, get_session


if 'seed' in sys.argv or not seeding.schema_exists():

    # create schema
    with get_engine() as engine:
        with engine.begin() as conn:
            conn.execute(DDL(f"CREATE SCHEMA IF NOT EXISTS {DeclarativeBase.metadata.schema}"))

            DeclarativeBase.metadata.drop_all(conn)
            DeclarativeBase.metadata.create_all(conn)

    # seed initial DB records
    with get_session() as session:
        seeding.seed_all(session)


app = get_app()
app.run(debug=True, host='0.0.0.0', port=5000)
