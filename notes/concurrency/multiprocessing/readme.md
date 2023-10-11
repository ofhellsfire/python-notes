# Multiprocessing Notes

The overhead of using `multiprocessing` is high because of all the serialization 
and deserialization that must happen between the parent and child processes.

## `ProcessPoolExecutor`

### Internals Mechanics on `map` Example

1. It takes each item from the iterable to `map` (for example: `pool.map(...)`)
2. It serializes it into binary data using the `pickle` module
3. It copies the serialized data from the main interpreter process to a child interpreter process over a local socket
4. It deserializes the data back into Python object using `pickle` in the child process
5. It imports the Python module containing the target function that has been passed to `map`
6. It runs the function on the input data in parallel with other child processes
7. It serializes the result back into bytes
8. It copies those bytes back through the socket
9. It deserializes the bytes back into Python object in the parent process
10. Finally it merges the results from multiple children into a single list to return

