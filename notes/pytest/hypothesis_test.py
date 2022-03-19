import pytest
from hypothesis import given, assume
from hypothesis.strategies import integers, text, datetimes, from_regex, builds, composite


class Person:
    def __init__(self, age: int):
        self.age = age

    def grow_older(self):
        if self.age > 100:
            raise ValueError()
        self.age += 1


def is_first_name(name: str) -> bool:
    if name is None or len(name) < 3:
        return False
    if not name.isalpha():
        return False
    if not name[0].isupper():
        return False
    if not name[1:].islower():
        return False
    return True


@composite
def first_names(draw):
    allowed_first_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    lower_letters_strategy = from_regex(regex=r"^[a-z]$", fullmatch=True)
    first_letter = draw(text(alphabet=allowed_first_letters, min_size=1, max_size=1))
    rest = draw(text(alphabet=lower_letters_strategy, min_size=2, max_size=10))
    return first_letter + rest

# --- tests

@given(builds(Person, age=integers(1, 100)))
def test_person_can_grow_older(person):
    current_age = person.age
    person.grow_older()
    person.age == current_age + 1


@given(first_names())
def test_is_first_name(first_name):
    assert is_first_name(first_name)