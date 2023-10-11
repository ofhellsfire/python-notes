"""
"""

def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)


if __name__ == "__main__":
    it = minimize()
    next(it)  # Prime the generator
    for i in (10, 20, 5, 33, 76, -1, 11):
        print(it.send(i))
