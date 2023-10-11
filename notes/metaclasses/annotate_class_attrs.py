"""
Example showing annotation of class attributes with metaclasses.

Here we assign names on descriptors automatically, instead of: `name = Field("some name")`
"""


class Field:

    def __init__(self):
        # the props below will be assigned by the metaclass
        self.name = None
        self.internal_name = None

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, "")
    
    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class Meta(type):

    def __new__(mcs, name, bases, attrs):
        for key, value in attrs.items():
            if isinstance(value, Field):
                # Metaclasses let us hook the `class`` statement directly and take
                # action as soon as a `class` body is finished
                value.name = key
                value.internal_name = f"_{key}"
        return super().__new__(mcs, name, bases, attrs)


class DatabaseRow(metaclass=Meta):
    pass


class Customer(DatabaseRow):
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()


if __name__ == "__main__":
    foo = Customer()
    print(foo, foo.__dict__)
    foo.first_name = "Maxim"
    print(foo, foo.__dict__)
