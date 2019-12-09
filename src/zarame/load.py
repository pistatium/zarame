from enum import EnumMeta
from typing import Type, TypeVar, Any, Iterable

from .utils import is_named_tuple, is_list_type, is_tuple_list_type

NO_KEY = '__NO_KEY__'


T = TypeVar('T')


def load(d: dict, klass: Type[T]) -> T:
    return _load(d, klass)


def _load(d: dict, klass: Type[T]) -> Any:

    if not hasattr(klass, '_field_types'):
        raise ValueError(f'klass must be subtype of NamedTuple')

    fields = klass.__annotations__
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

        if is_list_type(field_type):
            if not isinstance(value, Iterable):
                raise ValueError(f'{field} must be iterable. Actual: {type(value)}')
            tmp[field] = [_load(v, field_type.__args__[0]) for v in value]
            continue

        if is_tuple_list_type(field_type):
            if not isinstance(value, Iterable):
                raise ValueError(f'{field} must be iterable. Actual: {type(value)}')
            tmp[field] = tuple(_load(v, field_type.__args__[0]) for v in value)  # type: ignore  # FIXME
            continue

        if isinstance(field_type, EnumMeta):
            tmp[field] = field_type(value)
            continue

        if is_named_tuple(field_type):
            tmp[field] = _load(value, field_type)
            continue
        tmp[field] = value

    return klass(**tmp)  # type: ignore # FIXME
