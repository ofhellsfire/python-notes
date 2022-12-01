# Python's Exception Hooks

## Exception Hooks

Whenever exception is raised and isn't handled by `try/except` block, a function 
assigned to `sys.excepthook` is called. This function - called *Exception Hook* 
- is then used to output any relevant information to standard output using the 
- 3 arguments it receives - `type`, `value` and `traceback`.

