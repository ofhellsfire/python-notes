# Classes

## When to Use Instance Methods, `@classmethod`, `@staticmethod`

### When to Use `@classmethod`

We use class methods when we want to call it without creating an instance of the 
class. This is usually when we don't need instance information, but we need class 
information.

Also it is used often as alternative initializer.

Also the benefit of class methods is that we don't have to hardcode the class, 
thus allowing subclasses to use the methods too.

### When to Use `@staticmethod`

We use static methods when we don't need class or instance arguments, but the 
method is related to the class and it is convenient for the method to be in the 
class's namespace.
