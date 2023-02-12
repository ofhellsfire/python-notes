import argparse

import grpc

from generated import weather_pb2, weather_pb2_grpc


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", default=12345, help="port to use for connection")
    parser.add_argument("--lat", required=True, type=float, help="latitude")
    parser.add_argument("--lon", required=True, type=float, help="longitude")
    return parser.parse_args()


def run(port, lat, lon):
    with grpc.insecure_channel(f"localhost:{port}") as channel:
        stub = weather_pb2_grpc.WeatherInfoServiceStub(channel)
        response = stub.GetWeatherInfo(
            weather_pb2.Location(
                lat=lat,
                long=lon,
            )
        )
    print(
        f"Weather for lat: {lat}, lon: {lon} is:\n"
        f"Temperature: {response.temp},\n"
        f"Humidity: {response.humidity}%,\n"
        f"Probability of Precipitation: {response.precipitation}%,\n"
        f"Sky Cover: {response.skycover.decode('utf-8')}"
    )


if __name__ == '__main__':
    args = parse_args()
    run(port=args.port, lat=args.lat, lon=args.lon)
