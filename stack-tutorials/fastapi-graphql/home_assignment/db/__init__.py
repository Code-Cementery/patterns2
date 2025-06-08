# isort: skip_file
import functools

from sqlalchemy import inspect

from .sql import DecimalType, ArrowType
from .base import Base
from .asset import AssetEntity
from .fee import FeeEntity
from .user import UserEntity
from .label import LabelKeyEntity, LabelValueEntity
from .trade import TradeEntity


@functools.cache
def get_relationships(db_cls) -> set[str]:
    return set(inspect(db_cls).relationships.keys())


def get_unloaded_relationships(ent) -> set[str]:
    """
    Used for debugging lazy loading
    :param ent:
    :return:
    """
    return set(inspect(ent).unloaded)
