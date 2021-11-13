"""
Run test examples: 

`pytest -v -m baz notes/pytest/marker_test.py`
`pytest -v -m 'baz or foo' notes/pytest/marker_test.py`
`pytest -v -m 'bar and foo' notes/pytest/marker_test.py`
`pytest -v -m 'bar and not foo' notes/pytest/marker_test.py`
"""

import pytest


@pytest.mark.foo
@pytest.mark.bar
def test_uno():
    assert 1 > 0


@pytest.mark.foo
def test_dos():
    assert 2 > 0


@pytest.mark.bar
def test_tres():
    assert 3 > 0


@pytest.mark.baz
def test_cuatro():
    assert 4 > 0
