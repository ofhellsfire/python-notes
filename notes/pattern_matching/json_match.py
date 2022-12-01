"""
Note: only for 3.10+
"""

orders = [
    {"statusCode": 200, "id": 12335, "price": 235.80, "items": ["A", "B", "C", "D"]},
    {"statusCode": 200, "id": 12336, "price": 114.30, "items": ["B", "E", "F"]},
    {"statusCode": 500, "id": 0, "price": 0, "items": []},
    {"statusCode": 202, "id": 3456, "price": 35.00, "items": ["G"]},
    {"statusCode": 404, },
]


def process_json(response: dict):
    match response:
        case {"statusCode": 200, "id": _, "price": _, "items": [*products]}:  # Capture list
            print(f"Order contains following products: {products}")
        case {"statusCode": code, "id": _, "price": _, "items": _} if code >= 400:  # Capture and guard
            print(f"Failed with status code: {code}")
        case {"statusCode": _, "price": _, "items": _}:
            print("Missing required field: id")
        case {"statusCode": code, **fields}:
            print(f"Code: {code}, data: {fields}")


if __name__ == '__main__':
    for order in orders:
        process_json(order)
