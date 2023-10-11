# Multiprocessing Race Conditions

We can suffer race conditions when using process-based concurrency via `multiprocessing`.

> When threads or processes attempt to simultaneously access a shared
> resource, and the accesses can result in an error, we often say the program
> has a race condition, because the threads or processes are in a “race” to
> carry out an operation.

Two common classes of race conditions:

1. Race caused by accessing shared data or state
2. Race conditions caused due to timing

## Race Condition With Shared Data

Processes cannot share data directly, so race conditions is challenging, but still feasible.

A child process created using the "fork: start method (Linux) will get a copy 
of all global variables from the parent process, but any changes to the global 
variable in the child will have no effect on the global variable in the parent.

Processes do simulate shared memory using socket connections and files and may 
need to protect simulated shared program state or data from race conditions 
due to timing and concurrent modification.

There are 2 common ways for sharing Python objects and data between processes:

1. Host the object on a server process and allow processes to interact with it 
   indirectly via proxy objects - `multiprocessing.Manager`
2. Share primitive types (like integers, floats) between processes using shared 
   ctypes via `multiprocessing.Value` and `multiprocessing.Array`

Race conditions are possible with both ways above.

Also, it is possible for 2 processes to interact with other types of shared resources 
and suffer a reace condition as a result.

For example, if 2 or more processes attempt to write to the same file at the same 
time, the results may be unpredictable.

## Race Condition Due to Timing

Processes can suffer race conditions due to timing.

A synchronization primitive may be shared among processes and one or more processes 
may wait to be notified after another process has sent the notification message.

This type of race condition can occur with primitives that involve waiting: 
events, conditions, barriers.

## Process Safety

Process-safe refers to code that can be executed free of concurrency errors 
by multiple proceses concurrently.

To achieve that this may involve making correct use of synchronization primitives, like: 

- `Lock`
- `RLock`
- `Semaphore`
- `Event`
- `Condition`
- `Barrier`

Another way is to separate out responsibilities for interacting with a resource 
into a controlling process and having other processes send messages to the 
controlling process via `multiprocessing.Queue`.