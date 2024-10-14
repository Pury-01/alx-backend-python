#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async."""

import asyncio
import importlib
from typing import List
basic_async_syntax = importlib.import_module('0-basic_async_syntax')

wait_random = basic_async_syntax.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """execute wait_random n times concurrently."""
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
