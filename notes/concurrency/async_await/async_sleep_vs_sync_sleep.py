"""
async sleep vs sync sleep example

showing usage of sync libs in the async context does not make sense
"""

import asyncio
import time


async def uno():
    await asyncio.sleep(1)
    return 'uno'


async def tres():
    await asyncio.sleep(3)
    return 'tres'


async def sinco():
    await asyncio.sleep(5)
    return 'sinco'


async def uno_sync():
    time.sleep(1)
    return 'uno'


async def tres_sync():
    time.sleep(3)
    return 'tres'


async def sinco_sync():
    time.sleep(5)
    return 'sinco'


async def foo_sync():
    res = await asyncio.gather(uno_sync(), tres_sync(), sinco_sync())
    print(res)


async def foo_async():
    res = await asyncio.gather(uno(), tres(), sinco())
    print(res)


async def main():
    print('sync sleep')
    start = time.time()
    await foo_sync()
    print(f'Elapsed: {time.time() - start}')
    print('=' * 16)
    print('async sleep')
    start = time.time()
    await foo_async()
    print(f'Elapsed: {time.time() - start}')


if __name__ == '__main__':
    asyncio.run(main())
