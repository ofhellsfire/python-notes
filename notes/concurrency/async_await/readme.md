# Async/Await Notes

Async doesn't make your code parallel, it's more an optimization of idle time or concurrent.

`async`/`await` is a kind of syntactic sugar over coroutines, decorators and generators.

Every time we run `await` we give control back to python event loop to decide what to do in the meantime. In other words, `async` only "works" when you have to wait for IO operations.

In order to use `async/await` we cannot just declare all functions as async, we have to use libs that support async features.

## Unraveling Async/Await

Coroutines are functions that can be started, paused, and resumed. Whenever you invoke an `async` function you are getting a coroutine.

Whenever you `await`, you're asking for the event loop to handle that coroutine and return a result to you. Coroutines never awaited are never executed.

### Async

The `async def` evolved from `types.coroutine` decorator, which sets a flag on
the code object for the generator to distinguish it from any other plain generator.

So `async` functions are fundamentally generators.

## Await

The `await` expression evolved from `yield from`, but with 2 key tweaks:

- checking that the object is *awaitable*
- supporting awaitable objects which define `__await__()`
