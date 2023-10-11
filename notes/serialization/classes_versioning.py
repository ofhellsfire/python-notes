"""
Example of class versioning: when we need to have backward-incompatible changes 
to Python objects by removing fields.
"""

import copyreg
import pickle


class Foo:

    def __init__(self, num=0, name="default"):
        self.num = num
        self.name = name


def old_pickle_foo(foo):
    kwargs = foo.__dict__
    print(0, kwargs)
    return unpickle_foo, (kwargs,)


def pickle_foo(foo):
    kwargs = foo.__dict__
    kwargs["version"] = 2
    print(1, kwargs)
    return unpickle_foo, (kwargs,)


def unpickle_foo(kwargs):
    """It takes serialized data and parameters and returns the Foo object.

    A kind of tiny wrapper around the constructor.
    """
    print(2, kwargs)
    version = kwargs.pop("version", 1)
    if version == 1:
        kwargs.pop("new_field")
    return Foo(**kwargs)


if __name__ == "__main__":
    copyreg.pickle(Foo, old_pickle_foo)  # emulate old env before backward-incompatible changes

    foo = Foo(num=1, name="some name")  # create a backward-incompatible instance
    foo.new_field = 3.14  # emulating legacy class structure
    serialized_foo = pickle.dumps(foo)  # emulate saving old object

    # ... after some time, the Foo class has been changed

    copyreg.pickle(Foo, pickle_foo)

    foo2 = Foo(num=2, name="new some name")
    serialized_foo2 = pickle.dumps(foo2)
    deserialized_foo2 = pickle.loads(serialized_foo2)
    print(deserialized_foo2.__dict__)

    deserialized_foo = pickle.loads(serialized_foo)  # load old version object
    print(deserialized_foo.__dict__)
