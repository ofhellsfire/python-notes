"""
Example showing reference counting for GC
"""

import sys


foo = []
# 2 references, 1 from the foo var and 1 from getrefcount
print('module scope 1')
print('ref count:', sys.getrefcount(foo))


def bar(a):
    # 4 refs: from the foo var, function argument, getrefcount and Python's function stack
    print('function scope: inside bar')
    print('ref count:', sys.getrefcount(a))


bar(foo)
# 2 references, 1 from the foo var and 1 from getrefcount, the function scope is destroyed
print('module scope 2')
print('ref count:', sys.getrefcount(foo))
