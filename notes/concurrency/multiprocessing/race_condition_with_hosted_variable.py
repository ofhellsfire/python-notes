from multiprocessing import Process
from multiprocessing.managers import BaseManager
from time import sleep


class UnsafeCounter():
    def __init__(self, count):
        self._value = count
        
    def get(self):
        return self._value

    def increment(self):
        tmp = self._value
        sleep(0)  # allow context switch
        tmp = tmp + 1
        sleep(0)
        self._value = tmp

    def decrement(self):
        tmp = self._value
        sleep(0)
        tmp = tmp - 1
        sleep(0)
        self._value = tmp


# custom manager to support custom classes
class CustomManager(BaseManager):
    pass


def adder_task(counter):
    for i in range(1000):
        counter.increment()


def subtractor_task(counter):
    for i in range(1000):
        counter.decrement()


if __name__ == '__main__':
    CustomManager.register('UnsafeCounter', UnsafeCounter)
    with CustomManager() as manager:
        counter = manager.UnsafeCounter(0)
        adder_process = Process(target=adder_task, args=(counter,))
        subtractor_process = Process(target=subtractor_task, args=(counter,))
        adder_process.start()
        subtractor_process.start()
        adder_process.join()
        subtractor_process.join()
        print(f'Value: {counter.get()}')
        assert counter.get() == 0, 'Race condition detected!'
