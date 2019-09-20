from properties import Thermometer

class FancyThermometer(Thermometer):

    def __init__(self, temp, color='black', _max=None):
        super().__init__(temp, _max=_max)
        self.color = color


ft = FancyThermometer(25, _max=30)
print(f'Temperature: {ft.temp}')
try:
    ft.temp = 50
except ValueError as ex:
    print(f'Exception: {ex}')
ft.temp = -10
print(f'Temperature: {ft.temp}')
print(f'Temperature was accessed {ft._access_count} times')
print(f'Therm color is {ft.color}')
