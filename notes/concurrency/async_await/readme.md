# Async/Await Notes

`async`/`await` is a kind of syntactic sugar over coroutines, decorators and generators.

## Unraveling Async/Await

### Async

The `async def` evolved from `types.coroutine` decorator, which sets a flag on
the code object for the generator to distinguish it from any other plain generator.

So `async` functions are fundamentally generators.

## Await

The `await` expression evolved from `yield from`, but with 2 key tweaks:

- checking that the object is *awaitable*
- supporting awaitable objects which define `__await__()`