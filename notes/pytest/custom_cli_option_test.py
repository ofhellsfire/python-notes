"""

Example of accessing option is set from CLI:

```
cd notes/pytest
pytest --foo 12345 -vs custom_cli_option_test.py
```

"""

import pytest


@pytest.fixture()
def foo(pytestconfig):
    return pytestconfig.option.foo


def test_option(pytestconfig):
    print(f'"foo" option is set to: {pytestconfig.getoption("foo")}')


def test_option_dos(foo):
    print(f'"foo" option is set to: {foo}')
