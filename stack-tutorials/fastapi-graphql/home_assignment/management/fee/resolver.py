import decimal

import strawberry

from ..asset.resolver import Asset


@strawberry.type
class Fee:
    currency: Asset
    amount: decimal.Decimal
