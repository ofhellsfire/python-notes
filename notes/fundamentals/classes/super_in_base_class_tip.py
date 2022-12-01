# Non supered items

class Foo:

    def __init__(self):
        print('Foo class init')


class Bar:

    def __init__(self):
        print('Bar class init')


class Baz:

    def __init__(self):
        print('Baz class init')


class Uno(Foo, Bar, Baz):

    def __init__(self):
        super().__init__()
        print('Uno class init')


def non_supered_example():
    uno = Uno()


# ========

# Supered items

class Qux:

    def __init__(self):
        super().__init__()
        print('Qux class init')


class Zee:

    def __init__(self):
        super().__init__()
        print('Zee class init')


class Rua:

    def __init__(self):
        super().__init__()
        print('Rua class init')


class Dos(Qux, Zee, Rua):

    def __init__(self):
        super().__init__()
        print('Dos class init')


def supered_example():
    dos = Dos()

# ========

if __name__ == "__main__":
    non_supered_example()
    print('======')
    supered_example()
