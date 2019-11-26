# Demonstrates class-bound super proxy

class A:

    @staticmethod
    def foo():
        print('foo() from A')


class B(A):
    pass


class C:
    
    @staticmethod
    def foo():
        print('foo() from C')


class D(B):
    pass


class E(C):
    pass


class F(D, E):
    pass


super(D, F).foo()    # Will print: foo() from A
super(E, F).foo()    # Will print: foo() from C
super(A, F).foo()    # Will print: foo() from C
super(B, F).foo()    # Will print: foo() from A
