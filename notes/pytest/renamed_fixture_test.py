import pytest


@pytest.fixture(name='my_fixture')
def get_my_long_long_named_fixture():
    print('renamed fixture')


def test_uno(my_fixture):
    assert True
