# Demonstrates simple mixin


class BarkableMixin:

    def bark(self):
        print('Gav gav')


class RunnableMixin:

    def run(self):
        print('I am running')


class WaggableMixin:

    def wag(self):
        print('I am wagging my tail')


class Dog(BarkableMixin, RunnableMixin, WaggableMixin):

    def __init__(self, name):
        self.name = name


tuzik = Dog('Tuzik')
print(tuzik.name)   # Will print: Tuzik
tuzik.bark()        # Will print: Gav gav
tuzik.run()         # Will print: I am running
tuzik.wag()         # Will print: I am wagging my tail
