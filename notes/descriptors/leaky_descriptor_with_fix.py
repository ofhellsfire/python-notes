"""
Example showing leaky descriptor and acceptable fix.
"""

from weakref import WeakKeyDictionary


class LeakyDescriptor:

    def __init__(self):
        # the `_values` will hold a reference to every instance of `Foo`
        # that ever passed to `__set__()` over the lifetime of the program;
        # this causes instances to never have their reference count go to zero, 
        # preventing cleanup by the garbage collector.
        self._values = {}

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Value must be between 0 and 100")
        self._values[instance] = value


class NonLeakyDescriptor:

    def __init__(self):
        # to fix leaky descriptor we use `WeakKeyDictionary`, it will remove `Foo`
        # instances from its set of keys when the runtime knows it is holding the 
        # instance's last remaining reference in the program; python will do bookkeeping
        # and ensure that the `_values` dict will be empty when all `Foo` instances 
        # are no longer in use
        self._values = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Value must be between 0 and 100")
        self._values[instance] = value


class Foo:

    a = LeakyDescriptor()
    b = NonLeakyDescriptor()
