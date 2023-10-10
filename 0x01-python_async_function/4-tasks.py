#!/usr/bin/env python3

import asyncio
from typing import List


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n (int): number of times wait_random will be called
        max_delay (int): maximum delay value
    Returns:
        List[float]: list of all the delays
    """
    delays = []
    for i in range(n):
        delays.append(await task_wait_random(max_delay))
    return sorted(delays)
