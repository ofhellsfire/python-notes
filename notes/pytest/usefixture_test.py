"""

`usefixtures` for all tests in a class example:

pytest -sv notes/pytest/usefixture_test.py
"""

import pytest


@pytest.fixture
def quix():
    print('quix fixture')


@pytest.mark.usefixtures('quix')
class TestSomething():

    def test_uno(self):
        ...

    def test_dos(self):
        ...
