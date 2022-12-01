# Borg

The Borg pattern (also known as the Monostate pattern) is a way to
implement singleton behavior, but instead of having only one instance
of a class, there are multiple instances that share the same state. In
other words, the focus is on sharing state instead of sharing instance
identity.

In Python, you can implement Monostate in many ways, but the Borg design pattern is often best. 
Simplicity is its greatest strength. Since the `__dict__` of any instance can be re-bound, 
Borg rebinds it in its `__init__` to a class-attribute dictionary. 
Now, any reference or binding of an instance attribute will actually affect all instances equally.

## Example

```
class Borg:
    _shared = {}
    def __init__(self):
        self.__dict__ = self._shared
```
