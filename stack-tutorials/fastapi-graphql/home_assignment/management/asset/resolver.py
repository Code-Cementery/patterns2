import strawberry

from ...deps import GenieInfo
from .database import query_assets


@strawberry.type
class Asset:
    symbol: str
    name: str

    @classmethod
    def from_db_model(cls, asset):
        return Asset(
            symbol=asset.symbol,
            name=asset.name
        )


async def get_assets(info: GenieInfo) -> list[Asset]:
    with info.context.session_factory.begin() as session:
        assets = query_assets(session)
        return [Asset.from_db_model(asset) for asset in assets]
