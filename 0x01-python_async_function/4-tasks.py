#!/usr/bin/env python3
'''
takes code fron wait_n and alters it into a new function task_wait_n
'''

import asyncio
from typing import List
import importlib


tasks = importlib.import_module('3-tasks')
task_wait_random = tasks.task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Runs task_wait_random n times concurrently and returns the
    list of delays."""
    task = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*task)
    return sorted(delays)
