"""
Run test examples:

`pytest -v -s notes/pytest/autouse_fixture_test.py`
"""

import pytest


@pytest.fixture(autouse=True)
def foo():
    print('before foo fixture')
    yield 'foo'
    print('after foo fixture')


def test_uno():
    assert 10 > 0


def test_dos():
    assert 20 > 0


def test_tres():
    assert 30 > 0
