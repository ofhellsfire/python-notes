# Demonstrates super() built-in function usage

class Base:

    def __init__(self):
        print('Base init')

    def foo(self):
        print('Base.foo()')


class Sub(Base):

    def __init__(self):
        super().__init__()
        print('Sub init')

    def foo(self):
        print('Sub.foo()')

    def bar(self):
        super().foo()


base = Base()  # will print "Base init"
base.foo()     # will print "Base.foo()"

sub = Sub()    # will print "Sub init"
sub.foo()      # Will print "Sub.foo()"
sub.bar()      # Will print "Base.foo()"
