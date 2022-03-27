import asyncio


async def foo():
    return 'alala'


async def main():
    coro = foo()
    task = asyncio.create_task(coro)
    print(type(task))

    print(await task)


if __name__ == '__main__':
    asyncio.run(main())