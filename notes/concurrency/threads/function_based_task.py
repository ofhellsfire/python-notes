import threading
import time


results = []


def io_bound_task(a, b, c, d=0, name='default name'):
    print(f'Start "IO Bound Task: {name}"')
    time.sleep(2)
    res = {(a, b, c, d): a + b + c + d}
    print(res)
    results.append(res)


if __name__ == '__main__':
    threads = []
    for i in range(10):   
        thread = threading.Thread(
            target=io_bound_task,
            args=(i * 1, i * 2, i * 3,),
            kwargs={'d': i * 10, 'name': f'thread-{i}'},
            name=f'thread-{i}',
        )
        threads.append(thread)
    
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    
    print(f'Results: {results}')
