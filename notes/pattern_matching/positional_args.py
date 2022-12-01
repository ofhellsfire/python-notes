"""
Note: only for 3.10+
"""

class Location:
    """
    `__match_args__` class attribute allow us to specify tuple of instance 
    attributes in order in which they will be used as positional arguments. Not 
    all instance attributes have to be listed in `__match_args__`, so consider 
    putting only required args and drop out optional.

    Also if we use `dataclass` we get this feature out of the box.
    """
    __match_args__ = ("country", "city")

    def __init__(self, country, city):
        self.country = country
        self.city = city


def test_pos_args(location):
    match location:
        case Location("Russia", "Vladimir"):
            print("Privet Vladimir")
        case Location(_, "London"):
            print("There's London in several countries")
        case Location("China", _):
            print("Hello China")


if __name__ == "__main__":
    for loc in (
        Location("Russia", "Vladimir"),
        Location("Canada", "London"),
        Location("China", "Beijing"),
    ):
        test_pos_args(loc)
