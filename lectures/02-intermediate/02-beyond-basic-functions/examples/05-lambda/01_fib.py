def fib(stop=10, debug=False):
    a, b = 0, 1
    for _ in range(0, stop):
        if debug:
            print(a)
        a, b = b, a + b
    return a


print('Imperative style')
print(fib(10, debug=True))


def _fib(a, b, index=1, stop=10, debug=False):
    if index == stop:
        return a
    if debug:
        print(a)
    return _fib(a=b, b=(a + b), index=(index + 1), stop=stop, debug=debug)


def fib(stop=10, debug=False):
    return _fib(0, 1, 0, stop, debug)


print('Functional style')
print(fib(10, debug=True))


def fib2(n):
   if n <= 1:
       return n
   else:
       return fib2(n - 1) + fib2(n - 2)


print('Alt Functional style')
print(fib2(10))
