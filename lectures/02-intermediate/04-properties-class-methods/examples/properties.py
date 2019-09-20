class Thermometer:

    def __init__(self, temp, _max=None):
        self._temp = temp
        self.max = _max
        self._access_count = 0

    @property
    def temp(self):
        self._access_count += 1
        return self._temp

    @temp.setter
    def temp(self, value):
        if self.max and value > self.max:
            raise ValueError('Temperature is too large')
        self._temp = value


if __name__ == '__main__':
    therm = Thermometer(16, _max=30)
    print(f'Temperature: {therm.temp}')
    therm.temp = 0
    print(f'Temperature: {therm.temp}')
    try:
        therm.temp = 40
    except ValueError as ex:
        print(f'Exception: {ex}')
    print(f'Temperature was accessed {therm._access_count} times')
