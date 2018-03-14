# coding: utf-8

from typing import NamedTuple, List, Type, Optional


NO_KEY = '__NO_KEY__'


def convert(d, klass: Type[NamedTuple]):
    fields = klass._field_types
    for field, type in fields.items():
        tmp = {}
        value = d.get(field, NO_KEY)
        if value == NO_KEY:
            if type != Optional:
                raise ValueError(f'{field} is required.')
        if type == List:
            if not isinstance(value, list):
                raise ValueError(f'{field} must be list. Actual: {type(value)}')
            tmp[field] = [convert(v, type.__args__[0]) for v in value]
            continue
        if isinstance(type, NamedTuple):
            tmp[field] = convert(value, type)
            continue
        tmp[field] = value
        return klass(**tmp)
