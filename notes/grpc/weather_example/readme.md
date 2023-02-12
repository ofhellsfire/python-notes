# gRPC Weather Example

## Setup

### Using Linux

```
curl -OL https://github.com/protocolbuffers/protobuf/releases/download/v3.11.4/protoc-3.11.4-linux-x86_64.zip
unzip protoc-3.11.4-linux-x86_64.zip -d protoc3

# Move the binary to directory which is PATH
sudo mv protoc3/bin/* /usr/local/bin/

sudo mv protoc3/include/* /usr/local/include/

# Change owner
sudo chown $USER /usr/local/bin/protoc
sudo chown -R $USER /usr/local/include/google

# Test if it works
protoc --version
```

### Using Nix

```
nix-shell -p protobuf python311Full
```

### Python

```
python3 -m venv venv
source venv/bin/activate
pip install grpcio grpcio-tools
```

## Generate Client And Server Interfaces

```
python3 -m grpc_tools.protoc --python_out=/tmp/generated --grpc_python_out=/tmp/generated -I /path/to/project/proto *.proto
```

## Run Example

```
# Run Server
python app.py

# Run Client
python client.py --lat 1.2345 --lon -4.321
```