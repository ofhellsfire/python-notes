"""This demonstrates deadlock in action.

Thread A         Dictionary            Thread B


  wait  ------>    var_a  <---           set
                              \         /
                               =========
                              /         \
  set   ------>    var_b  <---           wait
                  

NOTE: if it doesn't go into deadlock, then just repeat execution or increase `COUNT` value.

NOTE: expected behaviour is hunging. To exit press Ctrl+C
"""

import threading


d = dict(var_a=0, var_b=0)
COUNT = 10000
shared_a_lock = threading.Lock()
shared_b_lock = threading.Lock()


def set_a_b():
    for _ in range(COUNT):
        shared_a_lock.acquire()
        shared_b_lock.acquire()
        d['var_a'] += 1
        d['var_b'] += 1
        shared_a_lock.release()
        shared_b_lock.release()


def set_b_a():
    for _ in range(COUNT):
        shared_b_lock.acquire()
        shared_a_lock.acquire()
        d['var_b'] -= 1
        d['var_a'] -= 1
        shared_b_lock.release()
        shared_a_lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=set_a_b)
    t2 = threading.Thread(target=set_b_a)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f'var A = {d["var_a"]}; var B = {d["var_b"]}')

