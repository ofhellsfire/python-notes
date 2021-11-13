import pytest


def test_exception():
    with pytest.raises(ZeroDivisionError) as ex:
        a = 4 / 0
    exception_msg = ex.value.args[0]
    assert exception_msg == 'division by zero'
