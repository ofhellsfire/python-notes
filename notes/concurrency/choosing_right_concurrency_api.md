# Choosing the Right Concurrency API

Python standard library offers 3 concurrency APIs:

- **multiprocessing** module for process-based concurrency (*multiprocessing* module)
- **threading** module for thread-based concurrency (*threading* module)
- **asyncio** module for coroutine-based concurrency (*asyncio* module)

One of the approach is to use 3 step process when choosing the right Python 
concurrency API for your project.

1. CPU-Bound vs IO-Bound (Multiprocessing vs Threading)
   1.1. Choosing between AsyncIO and Threading
2. Many Ad-hoc tasks vs One complex task?
3. Pools vs Executors?

## Step 1: CPU-Bound vs IO-Bound Tasks

Are the tasks mostly CPU-bound or IO-bound?

### CPU-Bound Tasks

A CPU-bound task is a type of task that involves performing a computation and 
does not involve IO. The operations only involve data in main memory and performing 
computations on or with that data. The limit on these operations is the speed of 
the CPU. CPUs are very fast and often there are more than one CPU.

### IO-Bound Tasks

An IO-bound task is a type of task that involves reading from or writing to a 
device, file, or socket connection. The operations involve input and output (IO), 
and the speed of these operations is bound by the device, hard drive, or network 
connection. Doing IO is very slow compared to the speed of CPUs.

Interacting with devices, reading and writing files, and socket connections 
involve calling instructions in your OS (the kernel), which will wait for the 
operation to complete. If this operation is the main focus for your CPU, such 
as executing in the main thread of your Python program, then your CPU is going 
to wait many milliseconds or seconds doing nothing. This is potentially billions 
of operations that it is prevented from executing.

IO examples:

- reading or writing a file from the hard drive
- reading or writing to stdout, stdin, stderr
- printing a document
- downloading or uploading a file
- querying a server
- querying a database
- taking a photo or recording a video

### Choose Python Concurrency API

In general, you should use process-based concurrency if you have a CPU-bound 
task and thread-based concurrency if you have an IO-bound task.

Multiprocessing is not suitable for tasks that send or receive a lot of data with 
other processes, because of the computational overhead added because all data 
shared between processes must be serialized.

The threading module is suitable for tasks that focus on reading or writing from 
an IO device with relatively little calculation. Threading is not suitable for 
tasks that perform a lot of CPU computation as the GIL prevents more than one 
Python thread from executing at a time. You can execute tens, hundreds, or thousands 
of thread-based tasks to maximize the capabilities of the underlying hardware as IO 
spends most of the time waiting.

## Step 1.1: Choosing between AsyncIO and Threading

You should use coroutine-based concurrency if you have many socket connections 
(or prefer asynchronous programming), and thread-based concurrency otherwise.

The asyncio module focuses on concurrent non-blocking IO for socket connections. 
For example, if your IO tasks are file-based, then asyncio would not be an 
appropriate choice, at least for this reason alone.

Coroutines are more lightweight than threads, therefore a single thread may host 
many more coroutines than a process may manage threads. For example, asyncio may 
allow thousands, tens of thousands or more coroutines for socket-based IO as 
opposed to hundreds to low thousands of threads in the threading API.

## Step 2: Many Ad-Hoc Tasks vs One Complex Task?

What we are thinking about at this decision point is whether you need to issue 
one or many ad-hoc tasks that may benefit from a pool of reusable workers. 
Otherwise, whether you need a single task where a pool of reusable workers would 
be overkill.

Another way to think about it is whether you have one or a few different but 
complex tasks like monitors, schedulers or similar that might live for a long 
time, such as the duration of the program. These would not be ad-hoc tasks, and 
may not benefit from a reusable pool of workers.

- Shorter-lived and/or many ad-hoc: use a thread or process pool
- Longer-lived and/or complex tasks: use the Thread or Process class

Additional considerations include:

- Heterogeneous vs Homogeneous Tasks: A pool is more appropriate for a diverse 
  set of tasks (heterogeneous), and Process/Thread class is appropriate for one 
  type of task (homogeneous)
- Reuse vs Single Use: A pool is appropriate for reusing the basis of concurrency, 
  e.g. reusing a thread or a process for many tasks. A Process/Thread class is 
  appropriate for a single use task, a long lived one.
- Multiple Tasks vs Single Task: A pool naturally supports many tasks issued in many 
  ways. A Process/Thread class only supports one type of task, once configured 
  or overriden.

Some examples:

- A `for` loop that calls a function many times with different arguments each 
  iteration may be appropriate for a thread pool as workers can be reused for each 
  task automatically as needed.
- A background task that monitors a resource may be appropriate for a Thread/Process 
  class as it is a long-running single task and specialized functionality perhaps 
  spread across many function calls.
- A script that downloads many files would be appropriate for a pool of workers 
  as each task is short in duration and there may be many more files than there 
  are workers, allowing reuse of workers and queuing of tasks to complete.
- A one-off task that maintains internal state and interacts with the main 
  program may be appropriate for Thread/Process class as the class can be overriden 
  to use instance variables for state and methods for modular functionality.

## Step 3: Pools vs Executors?

There are 2 main types:

1. Pool: multiprocessing.pool.Pool or multiprocessing.pool.ThreadPool
2. Executors: concurrent.futures.ThreadPoolExecutor or concurrent.futures.ProcessPoolExecutor

Both types provide pools of workers.

The similarities are:

- Both can execute ad-hoc tasks
- Support sync and async task execution
- Support for checking the status and waiting for async tasks
- Support callback functions for async tasks

Choosing one over the other will not make a big impact on your program.

The main difference is in the API, specifically minor differences in focus or 
in how tasks are handled. Differences are:

- Executors provide the ability to cancel issued tasks, but the Pool does not.
- Executors can work with collections of heterogeneous tasks, and the Pool cannot.
- Executors cannot forcefully terminate all tasks, and the Pool can.
- Executors do not provide multiple parallel versions of the `map()` function, and the Pool does.
- Executors provide the ability to access an exception raised in a task, and the Pool does not.

The Pool is focused on concurrent `for`-loops with many different versions of the `map()` 
(applying a function each argument in an iterable).

The Executors can do the same, but the focus is more on issuing ad-hoc tasks 
asynchronously and managing the collection of tasks.
