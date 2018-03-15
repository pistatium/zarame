# coding: utf-8

from typing import NamedTuple, List, Optional

from zarame import load


class Icon(NamedTuple):
    url: str


class User(NamedTuple):
    id: int
    name: str
    meta: dict
    email: Optional[str]
    icon: Icon


class Room(NamedTuple):
    id: int
    users: List[User]


def test_load_simple():
    icon = {'url': 'https://example.com/profile/taro/img.jpg'}
    converted = load(icon, Icon)
    assert converted.url == 'https://example.com/profile/taro/img.jpg'


def test_load_structured():
    room = {
        'id': 1000,
        'users': [{
                'id': 1,
                'name': 'Taro',
                'meta': {'class': 'A'},
                'icon': {'url': 'https://example.com/profile/taro/img.jpg'}
            }, {
                'id': 2,
                'name': 'Hanako',
                'meta': {},
                'email': 'hanako@example.com',
                'icon': {'url': 'https://example.com/profile/hanako/img.jpg'}
        }]
    }
    converted = load(room, Room)
    assert converted.id == 1000
    assert len(converted.users) == 2
    assert converted.users[0].id == 1
    assert converted.users[0].email is None
    assert converted.users[0].icon.url == 'https://example.com/profile/taro/img.jpg'
    assert converted.users[1].id == 2
    assert converted.users[1].email == 'hanako@example.com'
    assert converted.users[1].icon.url == 'https://example.com/profile/hanako/img.jpg'


def test_default_value():
    class A(NamedTuple):
        a: int = 0

    assert load({}, A) == A(a=0)
    assert load({'a': 1}, A) == A(a=1)
