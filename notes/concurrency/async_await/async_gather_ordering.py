"""
async gather ordering

showing that asyncio.gather() ordering improve performance for some cases where 
1) takes some CPU time 2) do IO 3) takes some CPU time again.

There is no difference in asyncio.gather() invocation if IO only.

Try to pass coroutines in asyncio.gather() ordered by the expected IO wait 
time descending. That is, the first argument should be the coroutine with 
the highest expected IO wait, and so on.
"""

import asyncio
import time


async def uno():
    time.sleep(1)            # Can be request preparation (CPU)
    await asyncio.sleep(1)   # Wait until remote service respond (IO)
    time.sleep(1)            # Can be response processing (CPU)
    return 'uno'


async def tres():
    time.sleep(1)
    await asyncio.sleep(3)
    time.sleep(1)
    return 'tres'


async def sinco():
    time.sleep(1)
    await asyncio.sleep(5)
    time.sleep(1)
    return 'sinco'


async def foo_unordered():
    res = await asyncio.gather(uno(), tres(), sinco())
    print(res)


async def foo_ordered():
    res = await asyncio.gather(sinco(), tres(), uno())
    print(res)


async def main():
    print('foo unordered')
    start = time.time()
    await foo_unordered()
    print(f'Elapsed: {time.time() - start}')
    print('=' * 16)
    print('foo ordered')
    start = time.time()
    await foo_ordered()
    print(f'Elapsed: {time.time() - start}')


if __name__ == '__main__':
    asyncio.run(main())
