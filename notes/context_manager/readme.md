# Context Manager Notes

## Multiple Context Managers

Example:

```
with A() as a, B() as b:
    pass
```

## `async with` Statement

The `async with` statement works similar to the regular `with` statement, but it requires an asynchronous context manager. In other words, it needs a context manager that is able to suspend execution in its enter and exit methods. Asynchronous context managers implement the special methods `.__aenter__()` and `.__aexit__()`, which correspond to `.__enter__()` and `.__exit__()` in a regular context manager.

The `async with ctx_mgr` construct implicitly uses `await ctx_mgr.__aenter__()` when entering the context and `await ctx_mgr.__aexit__()` when exiting it. This achieves async context manager behavior seamlessly.

