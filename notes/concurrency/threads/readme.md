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
