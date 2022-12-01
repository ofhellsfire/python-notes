"""
Note: only for 3.10+
"""

import builtins

foo = 'string'
bar = 3.14

def print_type(val):
    """
    NOTE: if we use `case str` it will trigger *capture pattern*, hence overriding 
    builtin `str` and making it a variable.
    Instead when we use `case str()` it will trigger a *class pattern* and tests 
    if variable in `match ...` is of the specified type.
    This also works only for 9 builtin types. If we want to match against other 
    builtin types we will need to use *Abstract Base Class* (like `collections.abc.Iterable(): ...`)
    """
    match val:
        case str():
            print(f"'{val}' is string")
        case float():
            print(f"'{val}' is float")

def print_raw_type(t):
    match t:
        case builtins.str:
            print(f"'{t}' is String")
        case builtins.int:
            print(f"'{t}' is Integer")


if __name__ == '__main__':
    types = (foo, bar)
    for t in types:
        print_type(t)

    for t in (str, int):
        print_raw_type(t)
