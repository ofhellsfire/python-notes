import random
import time

from generated import weather_pb2_grpc, weather_pb2


SKYCOVERS = (
    b"Clear",
    b"Half Cloudy",
    b"Cloudy"
)


class WeatherProvider(weather_pb2_grpc.WeatherInfoServiceServicer):

    def GetWeatherInfo(self, request, context):
        # here we emulate delay of getting data from weather stations
        time.sleep(random.randint(1, 5000) / 1000)

        return weather_pb2.WeatherInfo(
            temp=random.randrange(-15, 40),
            humidity=random.randrange(0, 100),
            precipitation=random.randrange(0, 100),
            skycover=random.choice(SKYCOVERS),
        )
