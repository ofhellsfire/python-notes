# Classes Tips

## Using `super()` in base classes

Using `super()` in the base class allows for cooperative multiple inheritance. 
Without it, the `__init__` calls of parent classes - after a non-supered class - 
are skipped.