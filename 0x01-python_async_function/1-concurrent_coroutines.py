import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n (int): number of times wait_random will be called
        max_delay (int): maximum value of delay
    Returns:
        List[float]: list of all the delays (float values) in ascending order
    """
    delays = []
    tasks = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    for task in tasks:
        delay = await task
        delays.append(delay)
    return sorted(delays)
