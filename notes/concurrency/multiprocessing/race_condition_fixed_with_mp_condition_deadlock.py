from time import sleep
from multiprocessing import Condition, Event, Process


def task(condition, event):
    sleep(1)
    print('Process: Waiting to be notified...', flush=True)
    with condition:
        print('Process: Ready', flush=True)
        event.set()
        condition.wait()
    print('Process: Notified', flush=True)


if __name__ == '__main__':
    condition = Condition()
    event = Event()
    process = Process(target=task, args=(condition, event))
    process.start()
    event.wait()
    sleep(0.5)
    print('Main: Notifying the process')
    with condition:
        condition.notify()
    process.join()
    print('Main: Done')
