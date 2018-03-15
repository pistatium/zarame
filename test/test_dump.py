# coding: utf-8

from typing import NamedTuple, Optional, List

from zarame import dump


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


def test_dump_simple():
    icon = Icon(url='https://example.com/profile/taro/img.jpg')
    dumped = dump(icon)
    assert dumped == {'url': 'https://example.com/profile/taro/img.jpg'}


def test_dump_structured():
    room = Room(
            id=1000,
            users=[
                User(
                    id=1,
                    name='Taro',
                    meta={'class': 'A'},
                    email=None,
                    icon=Icon(url='https://example.com/profile/taro/img.jpg')
                ),
                User(
                    id=2,
                    name='Hanako',
                    meta={},
                    email='hanako@example.com',
                    icon=Icon(url='https://example.com/profile/hanako/img.jpg')
                )
            ]
    )
    dumped = dump(room)
    assert dumped == {
        'id': 1000,
        'users': [{
            'id': 1,
            'name': 'Taro',
            'meta': {'class': 'A'},
            'email': None,
            'icon': {'url': 'https://example.com/profile/taro/img.jpg'}
        }, {
            'id': 2,
            'name': 'Hanako',
            'meta': {},
            'email': 'hanako@example.com',
            'icon': {'url': 'https://example.com/profile/hanako/img.jpg'}
        }]
    }