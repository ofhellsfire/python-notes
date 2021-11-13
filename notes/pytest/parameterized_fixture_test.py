"""
Parameterized Fixture Alternatives Examples

`pytest -sv notes/pytest/parameterized_fixture_test.py`
"""

import pytest


@pytest.fixture(
    params=[
        (1, 2, 3),
        (4, 5, 9),
        (6, 7, 13),
        (8, 9, 17),
    ]
)
def num_uno(request):
    return request.param


def test_uno(num_uno):
    a, b, expected = num_uno
    assert a + b == expected


# With static id
@pytest.fixture(
    params=[
        (1, 2, 3),
        (4, 5, 9),
        (6, 7, 13),
        (8, 9, 17),
    ], ids=['1+2', '4+5', '6+7', '8+9']
)
def num_dos(request):
    return request.param


def test_dos(num_dos):
    a, b, expected = num_dos
    assert a + b == expected


# With dynamic id with function
def id_func(fixture_val):
    return f'{fixture_val[0]}+{fixture_val[1]}={fixture_val[2]}'

@pytest.fixture(
    params=[
        (1, 2, 3),
        (4, 5, 9),
        (6, 7, 13),
        (8, 9, 17),
    ], ids=id_func
)
def num_tres(request):
    return request.param


def test_tres(num_tres):
    a, b, expected = num_tres
    assert a + b == expected
