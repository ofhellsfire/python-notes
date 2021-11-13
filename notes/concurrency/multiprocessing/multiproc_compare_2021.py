import time

import numpy as np

from concurrent.futures import ProcessPoolExecutor
from loky import get_reusable_executor
from mpi4py.futures import MPIPoolExecutor
import ray
from dask.distributed import Client
from p_tqdm import p_map
from pathos.multiprocessing import ProcessPool
from mpire import WorkerPool


def slow_fn(args):
    n = 10000
    y = 0
    for j in range(n):
        j = j / n
        for i, p in enumerate(args):
            y += j * (p ** (i + 1))
    return y / n


def slow_fn_malloc(args):
    n = 10000
    x = np.linspace(0, 1, n)
    y = np.zeros(n)
    for i, p in enumerate(args):
        y += x * (p ** (i + 1))
    return y.sum() / 1


def get_jobs(num_jobs=512, num_args=5):
    return [j for j in np.random.random((num_jobs, num_args))]


jobs = get_jobs()


if __name__ == '__main__':

    # 1: serial
    start_time = time.time()
    name = 'serial'
    print(f'Start {name.upper()} execution...')
    for job in jobs:
        slow_fn(job)
    print(f'Elapsed time for {name.upper()}: {time.time() - start_time}')
    print(f'\n{"=" * 53}\n')

    # 2: concurrent.futures.ProcessPoolExecutor
    start_time = time.time()
    name = 'concurrent.futures.ProcessPoolExecutor'
    print(f'Start {name.upper()} execution...')
    with ProcessPoolExecutor(max_workers=4) as executor:
        res = list(executor.map(slow_fn, jobs, chunksize=16))
    print(f'Elapsed time for {name.upper()}: {time.time() - start_time}')
    print(f'\n{"=" * 53}\n')

    # 3: loky
    start_time = time.time()
    name = 'loky'
    print(f'Start {name.upper()} execution...')
    executor = get_reusable_executor(max_workers=4)
    res = list(executor.map(slow_fn, jobs, chunksize=16))
    print(f'Elapsed time for {name.upper()}: {time.time() - start_time}')
    print(f'\n{"=" * 53}\n')

    # 4: mpi4py run it separately: mpiexec -n 8 python =-m mpi4py.futures yourfile.py
    start_time = time.time()
    name = 'mpi4py'
    print(f'Start {name.upper()} execution...')
    with MPIPoolExecutor() as executor:
        res = list(executor.map(slow_fn, jobs, chunksize=16))
    print(f'Elapsed time for {name.upper()}: {time.time() - start_time}')
    print(f'\n{"=" * 53}\n')

    # 5: ray
    start_time = time.time()
    name = 'ray'
    ray.init()
    workfn = ray.remote(slow_fn)
    print(f'Start {name.upper()} execution...')
    res = [workfn.remote(job) for job in jobs]
    ray.get(res)
    print(f'Elapsed time for {name.upper()}: {time.time() - start_time}')
    print(f'\n{"=" * 53}\n')
    ray.shutdown()

    # 6: dask
    start_time = time.time()
    name = 'dask'
    client = Client()
    print(f'Start {name.upper()} execution...')
    futures = client.map(slow_fn, jobs)
    res = client.gather(futures)
    print(f'Elapsed time for {name.upper()}: {time.time() - start_time}')
    print(f'\n{"=" * 53}\n')

    # 7: p_tqdm
    start_time = time.time()
    name = 'p_tqdm'
    print(f'Start {name.upper()} execution...')
    res = p_map(slow_fn, jobs)
    print(f'Elapsed time for {name.upper()}: {time.time() - start_time}')
    print(f'\n{"=" * 53}\n')

    # 8: pathos
    start_time = time.time()
    name = 'pathos'
    print(f'Start {name.upper()} execution...')
    pool = ProcessPool()
    res = pool.map(slow_fn, jobs, chunksize=16)
    print(f'Elapsed time for {name.upper()}: {time.time() - start_time}')
    print(f'\n{"=" * 53}\n')

    # 9: mpire
    start_time = time.time()
    name = 'mpire'
    print(f'Start {name.upper()} execution...')
    with WorkerPool(n_jobs=5) as pool:
        res = pool.map(slow_fn, jobs, chunk_size=16)
    print(f'Elapsed time for {name.upper()}: {time.time() - start_time}')
    print(f'\n{"=" * 53}\n')
