class Foo:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.call_count = 0

    def __call__(self):
        self.call_count += 1
        print(f'called! this instance was called {self.call_count} times')


foo_instance = Foo()
foo_instance()
foo_instance()
foo_instance()
