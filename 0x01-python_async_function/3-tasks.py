import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Args:
        max_delay (int): maximum delay (in seconds)
    Returns:
        asyncio.Task: an asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
