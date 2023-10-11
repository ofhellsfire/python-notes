from multiprocessing import Process, Value
from multiprocessing import Value



def adder(variable):
    for _ in range(1000):
        with variable.get_lock():
            variable.value += 1


def subtractor(variable):
    for _ in range(1000):
        with variable.get_lock():
            variable.value -= 1


if __name__ == '__main__':
    variable = Value('i', 0)
    adder_proc = Process(target=adder, args=(variable,))
    adder_proc.start()
    subtractor_proc = Process(target=subtractor, args=(variable,))
    subtractor_proc.start()
    print('Waiting for processes to finish...')
    adder_proc.join()
    subtractor_proc.join()
    print(f'Value: {variable.value}')
    assert variable.value == 0, 'Race condition detected!'
