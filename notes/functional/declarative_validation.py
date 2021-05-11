"""
`pip install toolz`

Pattern is applicative-style validation
"""


from dataclasses import dataclass
from functools import reduce
from toolz import curry
from typing import Any


@dataclass
class Valid:

    value: Any

    def is_valid(self):
        return True

    def apply(self, other):
        if other.is_valid():
            return Valid(self.value(other.value))
        else:
            return other

    def and_then(self, f):
        return f(self.value)


@dataclass
class Invalid:

    value: Any

    def is_valid(self):
        return False

    def apply(self, other):
        if other.is_valid():
            return self
        else:
            return Invalid(self.value + other.value)

    def and_then(self, f):
        return self


def validate_into(f, *args):
    return reduce(lambda a, b: a.apply(b), args, Valid(curry(f)))


@dataclass
class Person:
    name: str
    age: int


def validate_name(name):
    if not isinstance(name, str) or name == "":
        return Invalid(["name must be a non-empty string"])
    else:
        return Valid(name)


def validate_age(age):
    if not isinstance(age, int):
        return Invalid(["age must be an integer"])
    elif age < 10:
        return Invalid(["age must be at least 10"])
    else:
        return Valid(age)


def validate_andy(person):
    if person.name == "Andy" and person.age < 40:
        return Invalid(["Andy is too old"])
    else:
        return Valid(person)


def validate_lena(person):
    if person.name == "Lena" and person.age < 40:
        return Invalid(["Lena is too old"])
    else:
        return Valid(person)


def validate(data):
    return validate_into(
        Person,
        validate_name(data.get("name")),
        validate_age(data.get("age")),
    ).and_then(validate_andy).and_then(validate_lena)


if __name__ == '__main__':
    a = validate({'name': None, 'age': 'hello'})
    print(f'{a}, {a.is_valid()}')
    
    print(validate({'name': 'Andy', 'age': 38}))
    print(validate({'name': 'Lena', 'age': 18}))
    print(validate({'name': 'Andy', 'age': 45}))

    b = validate({'name': 'Lena', 'age': 42})
    print(f'{b}, {b.is_valid()}')

