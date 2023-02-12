from concurrent import futures
import argparse
import grpc

from generated import weather_pb2_grpc
from grpc_app import WeatherProvider


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", default=12345, help="port to bind for the server")
    return parser.parse_args()


class Server:

    @staticmethod
    def run(port):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
        weather_pb2_grpc.add_WeatherInfoServiceServicer_to_server(WeatherProvider(), server)
        server.add_insecure_port(f"[::]:{port}")
        print(f"Serving weather gRPC service at port: {port}")
        server.start()
        server.wait_for_termination()


if __name__ == '__main__':
    args = parse_args()
    Server.run(args.port)
