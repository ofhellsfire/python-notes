# Demonstrates code/implementation awareness of what code is being executed

import dis
import inspect
import multiple_context_managers


def inspect_funcs():
    funcs = inspect.getmembers(multiple_context_managers, inspect.isfunction)
    print(funcs)
    _, func = funcs[0]
    source = inspect.getsource(func)
    print(source)
    print(func.__code__.co_code)
    dis.dis(func)


inspect_funcs()