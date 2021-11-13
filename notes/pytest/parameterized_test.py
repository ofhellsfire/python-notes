"""
Parameterized Alternatives Examples
"""

import pytest


@pytest.mark.parametrize(
    'data',
    [
        (1, 2, 3),
        (4, 5, 9),
        (6, 7, 13),
        (8, 9, 17),
    ]
)
def test_uno(data):
    a, b, expected = data
    assert a + b == expected


@pytest.mark.parametrize(
    'a, b, expected',
    [
        (1, 2, 3),
        (4, 5, 9),
        (6, 7, 13),
        (8, 9, 17),
    ]
)
def test_dos(a, b, expected):
    assert a + b == expected


@pytest.mark.parametrize(
    'a, b, expected',
    [
        (1, 2, 3),
        (4, 5, 9),
        (6, 7, 13),
        (8, 9, 17),
    ],
    ids=['1+2', '4+5', '6+7', '8+9']
)
def test_tres(a, b, expected):
    assert a + b == expected


@pytest.mark.parametrize(
    'data',
    [
        pytest.param((1, 2, 3), id='1+2=3'),
        pytest.param((4, 5, 9), id='4+5=9'),
        pytest.param((6, 7, 13), id='6+7=13'),
        pytest.param((8, 9, 17), id='8+9=17'),
    ]
)
def test_tres(data):
    a, b, expected = data
    assert a + b == expected
