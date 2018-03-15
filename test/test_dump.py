# coding: utf-8
from test.test_load import User, Room
from zarame import dump


def test_dump_simple():
    user = User(id=1, name='Taro', meta={'class': 'A'}, email=None)
    dumped = dump(user)
    assert dumped == {'id': 1, 'name': 'Taro', 'meta': {'class': 'A'}, 'email': None}


def test_dump_structed():
    room = Room(
            id=1000,
            users=[
                User(id=1, name='Taro', meta={'class': 'A'}, email=None),
                User(id=2, name='Hanako', meta={}, email='hanako@example.com')
            ]
    )
    dumped = dump(room)
    assert dumped == {
        'id': 1000,
        'users': [
            {'id': 1, 'name': 'Taro', 'meta': {'class': 'A'}, 'email': None},
            {'id': 2, 'name': 'Hanako', 'meta': {}, 'email': 'hanako@example.com'}
        ]
    }