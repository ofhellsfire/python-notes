# Descriptor Notes

## @property

The big problem with the `@property` built-in is reuse: the methods it decorates 
can't be reused for multiple attributes of the same class and they can't be reused 
by unrelated classes.

## Attributes Access

### `__getattr__`

If the class defines `__getattr__`, that method is called every time an attribute 
can't be found in an object's instance dictionary.

Example:

```
class LazyDB:
    def __init__(self):
        self.exists = 33
    
    def __getattr__(self, name):
        print(f"Called __getattr__({name})")  # just for logging purpose
        default_name = f"Value for {name}"
        setattr(self, name, default_value)
        return value

data = LazyDB()
print(data.exists)
print(data.foo)
print(data.foo)
```

This example shows behavior that is helpful for use cases like lazily accessing 
schemaless data. `__getattr__` runs once to do the hard work of loading a property; 
all subsequent accesses retrieve the existing result, because the second time we 
access `foo` there isn't a call to `__getattr__`.

### `__getattribute__`

This method is called every time an attribute is accessed on an object, even when 
it does exist in the attribute dictionary.

Example:

```
class ValidatingDB:
    def __init__(self):
        self.exists = 33
    
    def __getattribute__(self, name):
        print(f"Called __getattribute__({name})")  # just for logging purpose
        try:
            return super().__getattribute__(name)
        except AttributeError:
            default_name = f"Value for {name}"
            setattr(self, name, default_value)
            return value

data = ValidatingDB()
print(data.exists)
print(data.foo)
print(data.foo)
```

Problem with `__getattribute__` is that it is called on every attribute access for 
an object, even when we may not want that to happen.

Also we may encounter recursion problem with `__getattribute__`: it access some attribute, 
which causes `__getattribute__` to run again, and so on. To avoid that: use `super().__getattribute__`

### `__setattr__`

This method allows us to intercept arbitrary attribute assignments. The `__setattr__` 
method is always called every time an attribute is assigned on an instance.

The same recursion issue presents with `__setattr__` (see `__getattribute__` note)
