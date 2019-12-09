from typing import Any, List, Tuple


def is_named_tuple(o: Any) -> bool:
    # FIXME:
    return hasattr(o, '_asdict')


def is_list_type(t) -> bool:
    if not hasattr(t, '__origin__'):
        return False
    # Python36: List, Python37+: list
    return t.__origin__ in (List, list)


def is_tuple_list_type(t) -> bool:
    """
    Allowed only `Tuple[Type1, ...]`
    :param t:
    :return:
    """

    if not hasattr(t, '__origin__'):
        return False
    # Python36: List, Python37+: list
    if not t.__origin__ in (Tuple, tuple):
        return False
    return t.__args__[1] == Ellipsis
