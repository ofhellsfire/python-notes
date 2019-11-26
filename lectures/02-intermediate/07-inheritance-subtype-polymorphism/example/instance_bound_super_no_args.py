# Demonstrates instance-bound super proxy without arguments


class A:

    def foo(self):
        print('foo() from A')


class B(A):
    pass


class C:

    def foo(self):
        print('foo() from C')


class D(B):
    pass


class E(C):
    pass


class F(D, E):
    pass


class G(F):

    def baz(self):
        super().foo()


g = G()
g.baz()    # Will print: foo() from A
