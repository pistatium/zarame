# coding: utf-8

from typing import Any


def is_named_tuple(o: Any) -> bool:
    # FIXME:
    return hasattr(o, '_asdict')
