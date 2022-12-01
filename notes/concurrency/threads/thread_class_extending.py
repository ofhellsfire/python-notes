import threading
import time



class MyThread(threading.Thread):

    def __init__(self, values, name):
        super().__init__()
        self.values = values
        self.result = None
        self.name = name
    
    def run(self):
        print(f'Start "IO Bound Task: {self.name}"')
        time.sleep(2)
        self.result = self._calc()

    def _calc(self):
        a, b, c, d = self.values
        return a + b + c + d


if __name__ == '__main__':
    threads = []
    for i in range(10):
        thread = MyThread(
            name=f'thread-{i}',
            values=(i * 1, i * 2, i * 3, i * 10),
        )
        threads.append(thread)
    
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    
    print(f'Results: {[t.result for t in threads]}')
