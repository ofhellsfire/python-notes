# Demonstrates some basic scope introspection

from pprint import pprint as pp


print('Globals:')
pp(globals())
a = 53
print('Globals:')
pp(globals())

print('Defining a new variable through globals()')
globals()['b'] = 3.14124
print('Globals:')
pp(globals())
print(b)


def report_scope(arg):
    a = 1024
    pp(locals(), width=10)


print('Locals:')
report_scope(166)


def print_person_details():
    name = 'Masha'
    age = 33
    country = 'Russia'
    print('{name} is {age} years old and she is from {country}'.format(**locals()))


print_person_details()
