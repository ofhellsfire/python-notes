from collections import namedtuple
import csv
from datetime import date


def defaults_example():
    Developer = namedtuple(
        "Developer",
        "name level language",
        defaults=["Junior", "Python"]
    )
    return Developer("John")


def module_example():
    """The motivation to add the module argument to namedtuple() in Python 3.6
    was to make it possible for named tuples to support pickling through
    different Python implementations.
    """
    CustomPoint = namedtuple("Point", "x y", module="custom")
    Point = namedtuple("Point", "x y")
    return Point(10, 20), CustomPoint(100, 200)


def create_from_iterable():
    Person = namedtuple("Person", "name age height")
    return Person._make(["Jane", 25, 1.75])


def convert_into_dict():
    Person = namedtuple("Person", "name age height")
    jane = Person("Jane", 25, 1.75)
    return jane._asdict()


def replace_fields():
    Person = namedtuple("Person", "name age height")
    jane = Person("Jane", 25, 1.75)
    # After Jane's birthday
    jane = jane._replace(age=26)
    return jane


def fields_attr():
    Person = namedtuple("Person", "name age height")
    ExtendedPerson = namedtuple(
        "ExtendedPerson",
        [*Person._fields, "weight"]
    )
    jane = ExtendedPerson("Jane", 26, 1.75, 67)
    print(jane)

    for field, value in zip(jane._fields, jane):
        print(field, "->", value)


def field_defaults_attr():
    Person = namedtuple(
        "Person",
        "name age height weight country",
        defaults=["Canada"]
    )
    return Person._field_defaults


def read_csv():
    with open("example.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        Employee = namedtuple("Employee", next(reader), rename=True)
        for row in reader:
            employee = Employee(*row)
            print(employee.name, employee.job, employee.email)


def subclassing_example():
    BasePerson = namedtuple(
        "BasePerson",
        "name birthdate country",
        defaults=["Canada"]
    )
    class Person(BasePerson):
        __slots__ = ()
        def __repr__(self):
            return f"Name: {self.name}, age: {self.age} years old."
        @property
        def age(self):
            return (date.today() - self.birthdate).days // 365
    jane = Person("Jane", date(1996, 3, 5))
    print(jane.age)


if __name__ == '__main__':
    print(defaults_example())
    p1, p2 = module_example()
    print(f'{p1} (type: {type(p1)}; {p2} (type: {type(p2)}')
    print(create_from_iterable())
    print(convert_into_dict())
    print(replace_fields())
    fields_attr()
    print(field_defaults_attr())
    read_csv()
    subclassing_example()

