# Demonstrates simple MRO example

class A:
    def foo(self):
        print(f'{self.__class__.__name__}:foo()')


class B(A):
    pass


class C:
    def foo(self):
        print('ololo')


class D(B):
    pass


class E(C):
    pass


class F(D, E):
    pass


print(F.__mro__)
f = F()
f.foo()          # Will print: F:foo()
