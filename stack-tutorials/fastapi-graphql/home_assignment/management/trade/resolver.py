import decimal
from typing import Optional

import strawberry
from graphql import GraphQLError

from ..fee import Fee
from ..label import Label
from ..scalars import ArrowType
from ..user import User
from ..utils import get_selection, camel_to_snake, get_selected_fields
from ..asset import Asset
from ..pagination import PageInfo, Connection, Edge, cursor_to_datetime, datetime_to_cursor
from ...deps import GenieInfo
from .database import query_trades_filtered, count_trades


MAX_TRADES_PER_QUERY = 1000


async def query_usd(info: GenieInfo) -> Asset:
    return Asset(symbol="OOF", name="Off tesomsz")


@strawberry.type
class Trade:
    base: Asset
    quote: Asset

    price: decimal.Decimal
    amount: decimal.Decimal

    labels: list[Label]
    user: User
    fee: Fee
    placedAt: ArrowType

    @classmethod
    def from_db_model(cls, trade, requested_fields):
        return Trade(
            base=trade.base if 'base' in requested_fields else None,
            quote=trade.quote if 'quote' in requested_fields else None,
            fee=trade.fee if 'fee' in requested_fields else None,
            user=trade.user if 'user' in requested_fields else None,
            labels=[],
            placedAt=trade.placed_at,
            price=trade.price,
            amount=trade.amount
        )


async def get_trades(info: GenieInfo, base: Optional[str] = strawberry.UNSET, first: int = 100, after: Optional[str] = strawberry.UNSET) -> Connection[Trade]:

    base = base if base != strawberry.UNSET else None
    after = after if after != strawberry.UNSET else None

    if after is not None:
        after = cursor_to_datetime(after)

    trades_count = None

    if first > MAX_TRADES_PER_QUERY:
        raise GraphQLError(f"Cannot request over {MAX_TRADES_PER_QUERY} trades per page")

    # todo: add validation error: missing asset type (nonexisting crypto symbol filtered)

    requested_fields = get_selected_fields(info, 'edges.node')

    with info.context.session_factory.begin() as session:
        if get_selection(info, 'totalCount') is not None:
            # if requested, provide DB count with same filter parameters
            trades_count = count_trades(session, base)

        if requested_fields:
            requested_columns = set(map(camel_to_snake, requested_fields))

            trades = query_trades_filtered(session, base, columns=requested_columns, after=after, limit=first+1)

            edges = [Edge(Trade.from_db_model(trade, requested_fields), datetime_to_cursor(trade.placed_at)) for trade in trades]
        else:
            trades = []
            edges = []

    return Connection(
        page_info=PageInfo(
            has_previous_page=False,
            has_next_page=len(trades) > first,
            start_cursor=edges[0].cursor if edges else None,
            end_cursor=edges[-2].cursor if len(edges) > 1 else None,
        ),
        totalCount=trades_count,
        edges=edges[:-1]
    )
