import time
import threading


def task():
    print('Start task')
    for i in range(1, 6):
        print('.' * i)
        time.sleep(0.5)
    raise Exception('Task exception')
    print('Task ends with a success')


if __name__ == '__main__':
    t = threading.Thread(target=task)
    t.start()
    print('Start main process')
    time.sleep(10)
    print('Main process success')
    t.join()
