import base64
from datetime import datetime
from typing import List, Generic, TypeVar, Optional, Type

import strawberry
from arrow import Arrow

GenericType = TypeVar("GenericType")


Cursor: Type = str


@strawberry.type
class PageInfo:
    has_next_page: bool
    has_previous_page: bool
    start_cursor: Optional[str]
    end_cursor: Optional[str]


@strawberry.type
class Edge(Generic[GenericType]):
    node: GenericType
    cursor: Cursor

    def __init__(self, node: GenericType, cursor: Cursor = None):
        self.node = node
        self.cursor = node.get_cursor() if cursor is None else cursor


@strawberry.type
class Connection(Generic[GenericType]):
    """Represents a paginated relationship between two entities
    """
    page_info: PageInfo
    edges: List[Edge[GenericType]]
    totalCount: Optional[int]

def cursor_to_datetime(cursor_b64: Cursor) -> datetime:
    return datetime.fromisoformat(base64.b64decode(cursor_b64.encode('ascii')).decode())

def datetime_to_cursor(dt: datetime | Arrow) -> Cursor:
    return base64.b64encode(dt.isoformat().encode('ascii')).decode()
