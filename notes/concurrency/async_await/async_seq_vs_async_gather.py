"""
async sequential vs async gather example

showing that sequential `await` invocation does nothing from the performance improvement point of view
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


async def foo_seq():
    print(await uno())
    print(await tres())
    print(await sinco())


async def foo_gather():
    res = await asyncio.gather(uno(), tres(), sinco())
    print(res)


async def main():
    print('async sequential')
    start = time.time()
    await foo_seq()
    print(f'Elapsed: {time.time() - start}')
    print('=' * 16)
    print('async gather')
    start = time.time()
    await foo_gather()
    print(f'Elapsed: {time.time() - start}')


if __name__ == '__main__':
    asyncio.run(main())
