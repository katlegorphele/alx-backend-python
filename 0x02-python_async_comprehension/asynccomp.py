from gen import genasync
import asyncio


async def async_comprehension():
    ran = [i async for i in genasync()]
    return ran


async def main():
    print(await async_comprehension())


if __name__ == '__main__':
    asyncio.run(main())
