"""

Retrieve stdout and stderr from code example:

```
cd notes/pytest
pytest -vs capsys_fixture_test.py
```
"""

import sys

import pytest


def foo():
    print('this is foo')


def bar():
    print('this is error', file=sys.stderr)


def test_foo(capsys):
    foo()
    out, err = capsys.readouterr()
    assert out.strip() == 'this is foo'


def test_bar(capsys):
    bar()
    out, err = capsys.readouterr()
    assert err.strip() == 'this is error'