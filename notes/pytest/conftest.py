import pytest


@pytest.fixture(autouse=True)
def common_fixture_a():
    print('common_fixture_a')


def pytest_addoption(parser):
    parser.addoption("--foo", action="store", help="some example option")
