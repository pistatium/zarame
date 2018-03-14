# zarame
Simple structural transducer using NamedTuple

## Usage

```python
from typing import NamedTuple, List, Optional

from zarame import load


class User(NamedTuple):
    id: int
    name: str
    meta: dict
    email: Optional[str]


class Room(NamedTuple):
    id: int
    users: List[User]


room = {
    'id': 1000,
    'users': [
        {'id': 1, 'name': 'Taro', 'meta': {'class': 'A'}},
        {'id': 2, 'name': 'Hanako', 'meta': {}, 'email': 'hanako@example.com'}
    ]
}

load(room, Room)

```

### Result
```
Room(
        id=1000, 
        users=[
            User(id=1, name='Taro', meta={'class': 'A'}, email=None),
            User(id=2, name='Hanako', meta={}, email='hanako@example.com')
        ]
)
```
