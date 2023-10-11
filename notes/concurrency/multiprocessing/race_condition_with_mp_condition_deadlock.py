from time import sleep
from multiprocessing import Condition, Process


def task(condition):
    sleep(1)
    print('Process: Waiting to be notified...', flush=True)
    with condition:
        condition.wait()
    print('Process: Notified', flush=True)


if __name__ == '__main__':
    condition = Condition()
    process = Process(target=task, args=(condition,))
    process.start()
    sleep(0.5)
    print('Main: Notifying the process')
    with condition:
        condition.notify()
    process.join()
    print('Main: Done')
