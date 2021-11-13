"""
Cache example:

```
cd notes/pytest
pytest -sv test_cache_example.py
```
"""

import pytest


def test_uno(cache):
    print('Hello from test_uno')
    print(f'Cache is: {cache.get("key", "Nothing")}')
    cache.set('key', 'uno-uno')


def test_dos(cache):
    print(f'Hello from test_dos')
    print(f'Cache is: {cache.get("key", "Nothing")}')
    cache.set('key', 'uno-uno; dos-dos')


def test_tres(cache):
    print(f'Hello from test_tres')
    print(f'Cache is: {cache.get("key", "Nothing")}')
    cache.set('key', 'uno-uno; dos-dos; tres-tres')