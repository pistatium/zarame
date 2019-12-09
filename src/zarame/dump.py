from typing import List, Dict, Union, Any, NamedTuple
from enum import Enum


def dump(instance: NamedTuple) -> Dict[str, Any]:
    d = instance._asdict()
    for k, v in d.items():
        if hasattr(instance, '_asdict'):
            d[k] = _dump(v)
    return d


def _dump(o: Any) -> Union[str, List[Any], Dict[str, Any]]:
    if isinstance(o, Enum):
        return o.value
    if isinstance(o, list):
        return [_dump(l) for l in o]
    if not hasattr(o, '_asdict'):
        return o
    d = o._asdict()
    for k, v in d.items():
        if hasattr(o, '_asdict'):
            d[k] = _dump(v)
    return d
