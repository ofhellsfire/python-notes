"""
Note: only for 3.10+
"""

from types import SimpleNamespace


class InSet(set):
    def __eq__(self, elem):
        return elem in self


if __name__ == '__main__':
    Produce = SimpleNamespace(
        fruit=InSet({"apple", "banana", "peach"}),
        vegetable=InSet({"cucumber", "lettuce", "onion"}),
    )

    food = "cucumber"

    """
    We may try to use simply `case fruit` and `case vegetable` directly, but 
    that won't work as it triggers *capture* pattern and assign `food` into `fruit` 
    and `vegetable`.
    """
    match food:
        case Produce.fruit:
            print(f'{food} is a fruit.')
        case Produce.vegetable:
            print(f'{food} is a vegetable.')
        case _:
            print('Unkown')
