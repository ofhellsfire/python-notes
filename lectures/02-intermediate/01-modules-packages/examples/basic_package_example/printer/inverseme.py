import sys


def foo(msg):
    return ''.join(reversed(msg))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Missing argument. Please provide some message')
        sys.exit(1)
    print(f'{foo(sys.argv[1])}')
    sys.exit(0)
