from typing import Optional


def foo(bar: int) -> Optional[int]:
    if bar > 0:
        return bar
    else:
        return None


def bar(baz: int) -> int:
    return baz * 100


if __name__ == '__main__':
    a = -3
    b = foo(a)
    if b is None:  # Unwrapping an Optional
        b = 0
    print(bar(b))
