import pytest


@pytest.fixture(autouse=True)
def common_fixture_c():
    print('common_fixture_c')
