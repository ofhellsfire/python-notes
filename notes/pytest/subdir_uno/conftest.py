import pytest


@pytest.fixture(autouse=True)
def common_fixture_b():
    print('common_fixture_b')
