# Coroutines

Coroutines work by enabling the code consuming a generator to `send` a value 
back into the generator function after each `yield` expression. The generator 
funciton receives the value passed to the `send` function as the result of the 
corresponding `yield` expression.

The generator function will seemingly run forever, making forward progress with 
each new call to `send` (see simple_example.py). Like threads, coroutines are independent 
functions that can consume inputs from their environment and produce resulting outputs. The 
difference is that coroutines pause at each `yield` expression in the generator 
function and resume after each call to `send` from the outside. This is magical mechanism of coroutines.

This behavior allows the code consuming the generator to take action after each `yield` 
expression in coroutine. The consuming code can use the generator's output values 
to call other functions and update data structures. Most importantly, it can advance 
other generator functions until their next `yield` expression. By advancing many 
separate generators in lockstep, they will all seem to be running simultaneously, 
mimicking the concurrent behavior of Python threads.

## Couroutines vs Threads

Threads are fine, but there can be some problems:

- Need for special coordination between each other to prevent race conditions, which 
  makes code harder to reason about than single-threaded code
- Threads takes ~ 8Mb per executing thread
- Threads take some time to start

Coroutines help to work around these problems. They let us have many seemingly 
simultaneous functions. They're implemented as extension to generators.

- the cost of starting a generator coroutine is a function call
- each coroutine uses less than 1 Kb of memory
