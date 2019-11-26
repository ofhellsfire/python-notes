# Demonstrates class-bound super proxy without arguments

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


class G(F):
    @classmethod
    def bar(cls):
        super().foo()


G.bar()    # Will print: foo() from A
