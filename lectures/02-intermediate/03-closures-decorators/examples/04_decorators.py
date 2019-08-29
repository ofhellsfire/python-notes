def escape_unicode(func):
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return ascii(result)
    return wrapped

@escape_unicode
def russian_city():
    return 'Нижневартовск'

print(russian_city())


def subtract_decor(func):
    def wrapped(*args, **kwargs):
        if len(args) < 2:
            raise Error('Too few arguments')
        return args[0] - args[1]
    return wrapped

@subtract_decor
def sum(a, b):
    return a + b

print(sum(20, 10))


# old style decorator
import time
from collections import deque

def timeit(func):
    def wrapped(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(time.time() - start)
        return result
    return wrapped

def digitalize(num):
    result = deque()
    while num > 0:
        result.appendleft(num % 10)
        num //= 10
    return result

def digitalize2(num):
    return [int(item) for item in list(str(num))]

digitalize = timeit(digitalize)
digitalize2 = timeit(digitalize2)

print(digitalize(12345678901234567890))
print(digitalize2(12345678901234567890))
