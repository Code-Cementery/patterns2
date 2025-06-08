from sqlalchemy import select
from sqlalchemy.orm import Session

from ...db import AssetEntity


def query_assets(session: Session) -> list[AssetEntity]:
    query = select(AssetEntity)

    return session.execute(query).scalars().fetchall()


def get_asset_by_symbol(session: Session, symbol) -> AssetEntity:
    query = select(AssetEntity) \
        .filter(AssetEntity.symbol == symbol)

    return session.execute(query).scalars().first()
