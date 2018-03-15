# coding: utf-8


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