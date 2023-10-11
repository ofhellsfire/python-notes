"""
This example shows how legacy pickled objects (for example game saves, etc.) 
can be loaded correctly.
"""

import pickle
import copyreg


class Foo:

    def __init__(self, num=0, name="default", new_field=3.14):
        self.num = num
        self.name = name
        self.new_field = new_field  # a new field


def pickle_foo(foo):
    kwargs = foo.__dict__
    return unpickle_foo, (kwargs,)


def unpickle_foo(kwargs):
    """It takes serialized data and parameters and returns the Foo object.

    A kind of tiny wrapper around the constructor.
    """
    return Foo(**kwargs)


if __name__ == "__main__":
    copyreg.pickle(Foo, pickle_foo)

    foo = Foo(num=1, name="some name")  # create a old legacy instance
    del foo.new_field  # emulating legacy class structure
    serialized_foo = pickle.dumps(foo)
    deserialized_foo = pickle.loads(serialized_foo)
    print(deserialized_foo.__dict__)

    # ... after some time, the Foo class has been changed

    foo2 = Foo(num=2, name="new some name", new_field=99.99)
    serialized_foo2 = pickle.dumps(foo2)
    deserialized_foo2 = pickle.loads(serialized_foo2)
    print(deserialized_foo2.__dict__)
