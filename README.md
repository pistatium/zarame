# zarame

<img src="https://repository-images.githubusercontent.com/125183142/d7c96200-18e8-11ea-961a-a5b9d203a6d5" width=400>

[![PyPI version](https://badge.fury.io/py/zarame.svg)](https://badge.fury.io/py/zarame) [![CircleCI](https://circleci.com/gh/pistatium/zarame/tree/master.svg?style=svg)](https://circleci.com/gh/pistatium/zarame/tree/master)


Simple structural converter using NamedTuple


## Usage

```python
from typing import NamedTuple, List, Optional
from enum import Enum

from zarame import load


class Status(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    DELETED = 'deleted'


class User(NamedTuple):
    id: int
    name: str
    email: Optional[str]


class Room(NamedTuple):
    status: Status
    users: List[User]


room = {
    'status': 'active',
    'users': [
        {'id': 1, 'name': 'Taro'},
        {'id': 2, 'name': 'Hanako', 'email': 'hanako@example.com'}
    ]
}

# Convert from dict to Room instance

instance = load(room, Room)
```

### Result
```
Room(
        status=Status.Active,
        users=[
            User(id=1, name='Taro', email=None),
            User(id=2, name='Hanako', email='hanako@example.com')
        ]
)
```
