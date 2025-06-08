from datetime import datetime

from sqlalchemy import select, func
from sqlalchemy.orm import Session, lazyload, load_only, undefer, subqueryload

from ...db import TradeEntity, get_relationships


def query_trades(session: Session) -> list[TradeEntity]:
    query = select(TradeEntity)

    results = session.execute(query)
    return results.scalars().fetchall()


def query_trades_filtered(session: Session, /, base_asset: str = None,
                          *, limit: int, after: datetime = None, columns: set = None) -> list[TradeEntity]:
    requested_relations = columns & get_relationships(TradeEntity)

    query = select(TradeEntity)

    # todo: this is a wrong approach
    # use this: https://strawberry.rocks/docs/guides/dataloaders

    for relation in requested_relations:
        query = query.options(subqueryload(relation))

    if base_asset is not None:
        query = query.filter(TradeEntity.base.has(symbol=base_asset)) \

    if after is not None:
        query = query.filter(TradeEntity.placed_at > after)

    query = query\
        .order_by(TradeEntity.placed_at)\
        .limit(limit)

    return session.execute(query).scalars().fetchall()


def count_trades(session: Session, /, base_asset: str = None):
    query = session.query(func.count())\
        .select_from(TradeEntity)

    if base_asset is not None:
        # todo: SQLAlchemy has a known bug where it generates count of a subquery for JOINs
        #       instead of a simple COUNT(*) query
        query = query.filter(TradeEntity.base.has(symbol=base_asset))

    return query.scalar()
