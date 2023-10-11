# Metaclasses Notes

Metaclasses let us intercept Python's `class` statement and provide special behavior each time a class is defined.

A class is an object, and like any other object, it's an instance of something: a metaclass. The default metaclass is `type`.

```
>>> class Foo:
...   pass
... 
>>> foo = Foo()
>>> type(foo)
<class '__main__.Foo'>
>>> type(Foo)
<class 'type'>
```

It's possible to create a class without `class` statement:

```
>>> MyClass = type("MyClass", (), {})
>>> MyClass
<class '__main__.MyClass'>
```

The `class` statement isn't just syntactic sugar, it does some extra things: like setting `__qualname__` and `__doc__` properties or calling `__prepare__`.

When you write: `class A: ...` you are actually not creating the class, 
you describe the class and `type` creates this class object for you.

Each class can have one metaclass, however this metaclass can subclass multiple metaclasses.

Since Python3.6 there is a hook available: `__init_subclass__` method. It is able to replace majority (if not all) metaclasses.

> It is important to follow the *rule of least surprise* and only use these mechanisms 
> to implement well-understood idioms.

## Custom Simple Metaclass Example

```
class Meta(type):
    pass

class Foo(metaclass=Meta):
    pass

>>> type(Foo)
<class '__main__.Meta'>
```

The metaclass has access to the name of the class, the parent classes it inherits from, 
and all of the class attributes that were defined in the `class` body. See simple_example.py

## Metaclasses And Magic Methods

Metaclasses rely on several magic methods so it's quite useful to know them.

When you define a magic method in your class the function will end up as a pointer in a struct that describes the class, 
in addition to the entry in `__dict__`. That struct has a field for each magic method, these fields are called *type slots* 
(NOTE: it is not relevant to `__slots__`).

## Attributes Lookup

TODO: add pics here

For magic methods the lookup is done on the class, directly in the big struct with the slots:

- Does the object's class have a slot for that magic method (roughly `object->ob_type->tp_<magicmethod>` in C code)? 
  If yes, use it. If it's `NULL` then the operation is not supported.

It's uncommon to see `__init__` being implemented in a metaclass because it's not that powerful - 
the class is already constructed when `__init__` is called.

## The `__new__` Method

The `__new__` method is the constructor (it returns the new instance) while `__init__` 
is just a initializer (the instance is already created when `__init__` is called).

So `__new__` method is looked up statically on class (in case when we create instance of the class), because 
metaclass can also have `__new__` method:

- `Foo.__new__` is used to create instances of `Foo`
- `type.__new__` is used to create the `Foo` class

## The `__prepare__` Method

This method is called before the `class` body is executed and it must return a dictionary-like object 
that's used as the local namespace for all the code from the `class` body.

This method doesn't have it's own type slot and it's looked up via the class attribute lookup.

`__prepare__` can return objects that are not dict instances, so you need to make sure your `__new__` handles that.

In other words, returned dictionary-like object is used for filling class attributes and its values. 
`attrs` (or `classdict`) attribute is passed into the metaclass `__new__` and `__init__` methods is 
the same object that is returned by `__prepare__`. The object must behaves like a dict and have at 
least the `__setitem__` method. This `__setitem__` method is called by Python for all variables 
set inside the declared class body itself.

That is, for an ordinary class, with no custom metaclass, the variables are recorded in a dictionary

## Subclasses Inherit the Metaclass

One advantage compared to class decorators is the fact that subclasses inherit the metaclass.

In the same tone of classes allowing you to have multiple baseclasses, each one of those baseclasses may have a different metaclass. But with a twist: everything has to be linear: the inheritance tree must have a single leaf.

```
>>> class Meta1(type): pass
... 
>>> class Meta2(type): pass
... 
>>> class Base1(metaclass=Meta1): pass
... 
>>> class Base2(metaclass=Meta2): pass
... 
>>> class Foo(Base1, Base2): pass
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases
```

## Known Metaclasses Use Cases

- Registration (adding a class to a data structure)
- Registering types for reverse lookups, where we need to map a simple identifier back to a corresponding class
- Class registration, which is helpful for building modular programs
- Refactoring (modifying class attributes or adding new ones)
- Avoiding decorators repetition or decorating all subclasses
- Validation of subclasses
- Registering subclass - extendable strategy pattern
- A declarative way of building GUI
- Changing behavior
- Class name modification (must)
- List of base classes modification (must)
- Verification that a class was defined correctly
- Annotating class attributes with metaclasses, before the class is fully defined
