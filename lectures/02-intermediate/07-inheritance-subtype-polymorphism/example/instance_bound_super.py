# Demonstrates instance-bound super proxy


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


f = F()
super(D, f).foo()    # Will print: foo() from A
super(E, f).foo()    # Will print: foo() from C
super(A, f).foo()    # Will print: foo() from C
super(B, f).foo()    # Will print: foo() from A
