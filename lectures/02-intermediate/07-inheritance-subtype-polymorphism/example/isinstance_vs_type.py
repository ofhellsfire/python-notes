# Demonstrates `isinstance()` vs `type()` for checking derived types

class Base:
    pass


class Foo(Base):
    pass


class Bar(Foo):
    pass


class Baz:
    pass


bar = Bar()
baz = Baz()


print(isinstance(bar, Base))  # True
print(isinstance(bar, Foo))   # True
print(isinstance(baz, Base))  # False


# NOTE: it can't test if object is derived type
print(type(bar) is Foo)   # False
print(type(bar) is Base)  # False
print(type(bar) is Bar)   # True
