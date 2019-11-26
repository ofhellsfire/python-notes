# Demonstrates failed MRO example

class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, A, C):  # Will raise exception
    pass
