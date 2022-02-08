def foo(a, b, c):
    print(a, b, c)


# keyword only parameters
# `*` means: all parameters to the right in the function signature can't be passed as positional arguments
def bar(a, *, b, c):
    print(a, b, c)


# positional only parameters
# `/` means: all parameters to the left of the `/`` are positional-only. Positional-only parameters can't be passed a keyword argument.
def baz(a, /, b, c):
    print(a, b, c)


# mixed positional only and keyword only parameters: more control on how function will be invoked
# advantage on using strict function params:
# - Less to consider when your function changes
# - Consistency between documentation and usage
def qux(a, /, *, b, c):
    print(a, b, c)


if __name__ == '__main__':
    foo(1, 2, 3)  # call function with positional args
    foo(c=3, a=1, b=2)  # call function with keyword args
    foo(1, 2, c=3)  # call function with positional and keyword args

    # bar(1, 2, 3)  # error: TypeError: bar() takes 1 positional argument but 3 were given
    bar(c=3, a=1, b=2)  # ok: call function with keyword args
    bar(1, c=3, b=2)  # ok: call function with positional and keyword args

    baz(1, 2, 3)  # ok: call function with positional args
    # baz(c=3, a=1, b=2)  # error: TypeError: baz() got some positional-only arguments passed as keyword arguments: 'a'
    baz(1, 2, c=3)  # ok: call function with positional and keyword args

    # qux(1, 2, 3)  # error: TypeError: qux() takes 1 positional argument but 3 were given
    # qux(c=3, a=1, b=2)  # error: TypeError: qux() got some positional-only arguments passed as keyword arguments: 'a'
    # qux(1, 2, c=3)  # error: TypeError: qux() takes 1 positional argument but 2 positional arguments (and 1 keyword-only argument) were given
    qux(1, c=3, b=2)  # ok: call function with positional and keyword args
