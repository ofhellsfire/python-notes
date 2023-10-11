# Mixin Notes

If you find that multiple inheritance gives you the convenience and encapsulation, then 
consider writing a mixin. A mixin is a small class that only defines a set of 
additional methods that a class should provide. Mixin classes don't define their 
own instance attributes nor require their `__init__` method to be called.

Mixins can be composed and layered to minimize repetitive code and maximize reuse.
