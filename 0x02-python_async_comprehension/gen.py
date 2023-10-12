# generator expression
# I would call it tuple comprehension

# gen object
import random
import asyncio
gen = (i for i in range(10))  # gen

print(type(gen))
# print(dir(gen))

print(next(gen))


# generator function


async def genasync():
    i = 0
    while i < 10:
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        i += 1


async def print_yielded_values():
    result = []
    async for i in genasync():
        result.append(i)
    print(result)

if __name__ == '__main__':
    asyncio.run(print_yielded_values())
