# Threading

## Function Based Task

The target task function is useful for executing one-off ad-hoc tasks that 
probably don't interact with external state other than passed-in arguments and 
do not return a value.

## Thread Class Extending

Overriding the `threading.Thread` class offers more flexibility than calling 
a target function. It allows the object to have multiple functions and to have 
object member variables for storing state.

Extending the `threading.Thread` class is suited for longer-lived tasks and 
services within an application.

## Race Conditions

The Python interpreter enforces fairness between all of the threads that are 
executing to ensure they get a roughly equal amount of processing time. To do this, 
Python will suspend a thread as it's running and will resume another thread in turn. 
The problem is that we don't know exactly when Python will suspend our threads. 
A thread can be paused a halfway through what looks like an atomic operation, which 
can lead to race conditions and side effects in case threads work on the same source.
