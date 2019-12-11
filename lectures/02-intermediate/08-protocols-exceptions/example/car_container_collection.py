# Demonstrates simple collection protocol implementation by Car container example implemented as a deque wrapper

# NOTE: Don't use it production, for demo purpose only


from collections import deque


class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __repr__(self):
        return (f'Car(brand="{self.brand}", '
                f'model="{self.model}", '
                f'year="{self.year}")')


def ensure_car(func):
    def inner(*args):
        if not all(isinstance(item, Car) for item in args[1:]):
            raise TypeError('Not a Car type')
        return func(*args)
    return inner


class CarContainer:

    def __init__(self, cars=None):
        self._cars = deque(cars) if cars else deque()
        self._index = 0

    def __contains__(self, search):  # don't do that in production
        values = set()
        for car in self._cars:
            attrs = [item for item in dir(car) if not item.startswith('__')]  # not reliable
            for attr in attrs:
                values.add(getattr(car, attr))
        return search in values

    def __len__(self):
        return len(self._cars)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index >= len(self._cars):
            raise StopIteration
        result = self._cars[self._index]
        self._index += 1
        return result

    def __getitem__(self, index):
        if isinstance(index, slice):
            return tuple(self._cars)[index]  # deque doesn't support slicing
        return self._cars[index]

    def __reversed__(self):
        return reversed(self._cars)

    def __add__(self, other):
        if not isinstance(other, CarContainer):
            return NotImplemented
        return CarContainer(self._cars + other._cars)

    @ensure_car
    def append(self, car):
        self._cars.append(car)

    @ensure_car
    def prepend(self, car):
        self._cars.appendleft(car)


gaz = Car('ГАЗ', '24', '1985')
bmw = Car('BMW', '535', '2010')
toyota = Car('Toyota', 'Rav 4', '2018')

container = CarContainer()
container.append(gaz)
container.append(bmw)
container.append(toyota)
print(f'Check if brand "BMW" is in the container: {"BMW" in container}')
print(f'Check if a car manufactured in "2018" is in the container: {"2018" in container}')
print(f'Check if model "Camry"" is in the container: {"Camry" in container}')
print(f'There are {len(container)} cars in the container')
print(f'Get container item by index, where index = 1: {container[1]}')
print(f'Get several container items as tuple by slicing, where slice = [1:]: {container[1:]}')

print('Reverse items in the container and print those')
for item in reversed(container):
    print(item)

print('Adding two containers')
other_container = CarContainer([Car('Ford', 'Focus', '2015')])
new_container = container + other_container
for item in new_container:
    print(item)
