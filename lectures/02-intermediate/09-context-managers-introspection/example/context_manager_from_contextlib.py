# Demonstrates example of context manager that is created by `contextlib.contextmanager`

import contextlib


@contextlib.contextmanager
def foo():
    print('inside enter')
    try:
        yield 'inside with block'
        print('inside normal exit')
    except:
        print('inside exceptional exit')
        raise


with foo() as f:
    print(f)
    print('inside with body (explicit)')


with foo() as f:
    print(f)
    print('inside with body (explicit)')
    raise Exception('some error')
