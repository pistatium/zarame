# coding: utf-8
from enum import Enum, EnumMeta
from typing import List, Type, TypeVar

from .utils import is_named_tuple

NO_KEY = '__NO_KEY__'


T = TypeVar('T')


def load(d: dict, klass: Type[T]) -> T:

    if not hasattr(klass, '_field_types'):
        raise ValueError(f'klass must be subtype of NamedTuple')

    fields = klass._field_types
    tmp = {}

    for field, field_type in fields.items():
        value = d.get(field, NO_KEY)
        if value == NO_KEY:
            # Primitive
            if not hasattr(field_type, '__args__'):
                continue
            # Not Optional
            if type(None) not in list(field_type.__args__):
                raise ValueError(f'{field} is required.')
            value = None

        if hasattr(field_type, '__origin__') and field_type.__origin__ == List:
            if not isinstance(value, list):
                raise ValueError(f'{field} must be list. Actual: {type(value)}')
            tmp[field] = [load(v, field_type.__args__[0]) for v in value]
            continue

        if isinstance(field_type, EnumMeta):
            tmp[field] = field_type(value)
            continue

        if is_named_tuple(field_type):
            tmp[field] = load(value, field_type)
            continue
        tmp[field] = value

    return klass(**tmp)
