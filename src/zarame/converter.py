# coding: utf-8

from typing import NamedTuple, List, Type, Optional


NO_KEY = '__NO_KEY__'


def load(d: dict, klass: Type[NamedTuple]):
    fields = klass._field_types
    tmp = {}
    for field, field_type in fields.items():
        value = d.get(field, NO_KEY)
        if value == NO_KEY:
            if type(None) not in list(field_type.__args__):
                raise ValueError(f'{field} is required.')
            value = None

        if hasattr(field_type, '__origin__') and field_type.__origin__ == List:
            if not isinstance(value, list):
                raise ValueError(f'{field} must be list. Actual: {type(value)}')
            tmp[field] = [load(v, field_type.__args__[0]) for v in value]
            continue

        if isinstance(type, NamedTuple):
            tmp[field] = load(value, field_type)
            continue
        tmp[field] = value

    return klass(**tmp)


def dump(instance):
    if isinstance(instance, list):
        return [dump(l) for l in instance]
    if not hasattr(instance, '_asdict'):
        return instance
    d = instance._asdict()
    for k, v in d.items():
        if hasattr(instance, '_asdict'):
            d[k] = dump(v)
    return d

