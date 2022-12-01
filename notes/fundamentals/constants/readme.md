# Constants

Python doesn't have a dedicated syntax for defining constants. Python constants 
are variables that never change.

The Python community has adopted a naming convention for constants: use uppercase letters.

## Constants Organization

A common strategy for organizing and managing constants is creating a dedicated 
module which holds all of project constants.

```
prj/
|---- __init__.py
|---- my_module.py
|---- constants.py
```

## Type-Annotating Constants

Since Python 3.8, the `typing` module includes a `Final` class that allows us to 
type-annotate constants.

You have to use static type checker (like *mypy*) to check if your constants are not 
being reassigned.

```
from typing import Final

MAX_SPEED: Final[int] = 300
DEFAULT_COLOR: Final[str] = "\033[1;34m"
ALLOWED_BUILTINS: Final[tuple[str, ...]] = ("sum", "max", "min", "abs")
```

## Strict Constants Alternatives

- `__slots__` attribute
- `@property` decorator
- `namedtuple()` factory function
- `@dataclass` decorator
- `__setattr__()` special method
