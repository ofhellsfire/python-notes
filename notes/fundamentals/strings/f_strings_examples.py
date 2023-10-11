"""
f-strings examples
"""

# Arbitrary Expressions
print(f"{2 * 53}")


# Braces Escaping
print(f"{{70 + 4}}", f"{{{70 + 4}}}")


# Date and Time Formatting
from datetime import datetime as dt

print(f"{dt.now():%d/%b/%Y %T}")


# Percentage Formatting
print(f"{50 / 104:.2%}")


# Variable Names and Debugging (python 3.8+)
x = 1
y = 3.14
z = "ololo"

print(f"{x=}, {y=}, {z=}")


# Multiline f-Strings
name = "Alex"
profession = "Worker"
affiliation = "Ford"
message = (
    f"Hi {name}. "
    f"You are a {profession}. "
    f"You were in {affiliation}."
)
print(message)


# __repr__ and __str__
class Foo:

    def __str__(self):
        return 'Foo class from str'

    def __repr__(self):
        return '<Foo>()'

foo = Foo()
print(f"{foo}")
print(f"{foo!r}")


# Superior Performance
"""
$ python3 -m timeit -s 'x, y = "Hello", "World"' 'f"{x} {y}"'
5000000 loops, best of 5: 63 nsec per loop
$ python3 -m timeit -s 'x, y = "Hello", "World"' '"%s %s" % (x, y)'
2000000 loops, best of 5: 150 nsec per loop
$ python3 -m timeit -s 'x, y = "Hello", "World"' '"{} {}".format(x, y)'
1000000 loops, best of 5: 203 nsec per loop
"""


# Full Power of Formatting Spec
text = "hello world"

# Center text:
print(f"{text:^15}")

number = 1234567890.123456
# Set separator
print(f"{number:,.3f}")

number = 123
# Add leading zeros
print(f"{number:08}")


# Nested F-Strings
import decimal

width = 8
precision = 3
value = decimal.Decimal("42.12345")
print(f"output: {value:{width}.{precision}}")


# Conditionals Formatting
value = decimal.Decimal("42.12345")
print(f'Result: {value:{"4.3" if value < 100 else "8.3"}}')
value = decimal.Decimal("142.12345")
print(f'Result: {value:{"4.2" if value < 100 else "8.3"}}')


# Lambda Expressions
print(f"{(lambda x: x**2)(3)}")

