# coding: utf-8

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


def test_load_simple():
    user = {'id': 1, 'name': 'Taro', 'meta': {'class': 'A'}}
    converted = load(user, User)
    assert converted.id == 1
    assert converted.name == 'Taro'
    assert converted.meta == {'class': 'A'}
    assert converted.email is None


def test_load_structed():
    room = {
        'id': 1000,
        'users': [
            {'id': 1, 'name': 'Taro', 'meta': {'class': 'A'}},
            {'id': 2, 'name': 'Hanako', 'meta': {}, 'email': 'hanako@example.com'}
        ]
    }
    converted = load(room, Room)
    assert converted.id == 1000
    assert len(converted.users) == 2
    assert converted.users[0].id == 1
    assert converted.users[0].email is None
    assert converted.users[1].id == 2
    assert converted.users[1].email == 'hanako@example.com'
