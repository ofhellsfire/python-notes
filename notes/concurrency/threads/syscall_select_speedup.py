"""
Just a simple example of using blocking I/O via `select` system calls and speedup by threads.

When you face to do blocking I/O and computation simultaneously, it's time to consider moving 
your system calls to threads.
"""

import select
import threading
import time


def slow_systemcall():
    return select.select([], [], [], 0.1)


def serial_task():
    start = time.time()
    for _ in range(5):
        slow_systemcall()
    print(f"Serial time elapsed: {time.time() - start:.2f}")


def parallel_task():
    start = time.time()
    threads = []
    for _ in range(5):
        thread = threading.Thread(target=slow_systemcall)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    print(f"Parallel time elapsed: {time.time() - start:.2f}")


if __name__ == "__main__":
    serial_task()
    parallel_task()