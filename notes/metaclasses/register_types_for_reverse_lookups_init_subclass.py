"""
Example of registering types for reverse lookups via __init_subclass__ for custom JSON serializing/deserializing
"""

import json


registry = {}


def register_class(target_class):
    registry[target_class.__name__] = target_class


def deserialize(data):
    params = json.loads(data)
    name = params["class"]
    target_class = registry[name]
    return target_class(*params["args"], **params["kwargs"])


class Serializable:

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __init_subclass__(cls, **kwargs):
        register_class(cls)
        super().__init_subclass__(**kwargs)


    def serialize(self):
        return json.dumps(
            {
                "class": self.__class__.__name__,
                "args": self.args,
                "kwargs": self.kwargs,
            }
        )

class Point3D(Serializable):

    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f"Point3D(x={self.x}, y={self.y}, z={self.z})"


if __name__ == "__main__":
    p = Point3D(10, 20, z=30)
    print(f"{p=}")
    data = p.serialize()
    print(f"{data}")
    print(f"Deserialized data: {deserialize(data)}")
