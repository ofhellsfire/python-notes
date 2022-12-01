"""
Shows that only last folder in `makedirs` is created with the given mode for Python 3.7+.
"""

import os
import stat


if __name__ == '__main__':
    try:
        os.system("rm -r /tmp/foo")
    except:
        pass
    os.makedirs('/tmp/foo/bar/baz', mode=0o700)
    baz_mode = stat.S_IMODE(os.stat('/tmp/foo/bar/baz').st_mode)
    assert baz_mode == 448, f'baz mode is {baz_mode}'
    bar_mode = stat.S_IMODE(os.stat('/tmp/foo/bar').st_mode)
    assert bar_mode == 448, f'bar mode is {bar_mode}'
    foo_mode = stat.S_IMODE(os.stat('/tmp/foo').st_mode)
    assert foo_mode == 448, f'foo mode is {foo_mode}'
