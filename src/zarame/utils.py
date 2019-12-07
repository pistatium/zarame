from typing import Any, List


def is_named_tuple(o: Any) -> bool:
    # FIXME:
    return hasattr(o, '_asdict')


def is_list_type(t) -> bool:
    if not hasattr(t, '__origin__'):
        return False
    # Python36: List, Python37+: list
    return t.__origin__ in (List, list)
