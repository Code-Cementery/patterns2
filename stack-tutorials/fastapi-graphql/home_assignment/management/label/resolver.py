import strawberry


@strawberry.type
class Label:
    key: str
    value: str
