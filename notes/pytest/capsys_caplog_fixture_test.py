"""

Retrieve stdout and stderr from code example:

```
cd notes/pytest
pytest -vs capsys_fixture_test.py
```
"""

import logging
import sys

import pytest


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)


def foo():
    print('this is foo')


def bar():
    print('this is error', file=sys.stderr)


def baz():
    logger.info("test log message")


def test_foo(capsys):
    foo()
    out, err = capsys.readouterr()
    assert out.strip() == 'this is foo'


def test_bar(capsys):
    bar()
    out, err = capsys.readouterr()
    assert err.strip() == 'this is error'


def test_baz(caplog):
    caplog.clear()
    with caplog.at_level(logging.INFO, logger=__name__):
        baz()
        for record in caplog.records:
            if 'test log message' in record.message:
                break
        else:
            assert False, "Missing expected log message"
