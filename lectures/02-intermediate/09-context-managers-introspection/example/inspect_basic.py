# Demonstrates some basic inspect functionality

import inspect
import context_manager_practical


a = 100
b = 'my string'

def foo():
    print('inside foo')
    a = 200

class Bar:

    def __init__(self, count):
        self.count = count

    def baz(self):
        return f'inside baz() with {self.count}'


print(inspect.ismodule(context_manager_practical))
print()
print(inspect.getmembers(context_manager_practical))
print()
print(inspect.getmembers(context_manager_practical, inspect.isclass))
print()
print(inspect.getmembers(context_manager_practical.Connection, inspect.isfunction))
method_sig = inspect.signature(context_manager_practical.Connection._commit_transaction)
print(method_sig.parameters)
