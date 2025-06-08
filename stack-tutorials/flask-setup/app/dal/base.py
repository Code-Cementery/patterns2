from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

from app.cfg import get_db_cfg

metadata_ = MetaData(schema=get_db_cfg().db_schema)
Base = declarative_base(metadata=metadata_)
