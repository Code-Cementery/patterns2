import re

from strawberry.types.nodes import Selection

from ..deps import GenieInfo


def get_base_selection(info: GenieInfo) -> Selection:
    return get_selected_field(info.selected_fields, info.field_name)

def get_selected_field(sel: list[Selection], field_name) -> Selection:
    return next(filter(lambda x: x.name == field_name, sel), None)

def get_selection(info: GenieInfo, path: str) -> Selection | None:
    base = get_base_selection(info)

    try:
        for field_name in path.split('.'):
            base = get_selected_field(base.selections, field_name)
    except:
        return None

    return base

def get_selected_fields(info: GenieInfo, path: str) -> set[Selection]:
    node_selection = get_selection(info, 'edges.node')

    if not node_selection:
        return set()
    return set(map(lambda x: x.name, node_selection.selections))

def camel_to_snake(name):
    name = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', name).lower()
