# Demonstrates multiple context managers

import contextlib


@contextlib.contextmanager
def nest_test(name):
    print(f'Entering {name}')
    yield name
    print(f'Exiting {name}')

if __name__ == '__main__':
    with nest_test('outer') as n1, nest_test(f'inner, nested in {n1}'):
        print('BODY')
