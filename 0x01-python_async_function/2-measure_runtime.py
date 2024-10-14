#!/usr/bin/env python3
"""measure the runtime."""


import time
import importlib
import asyncio

concurrent_coroutines = importlib.import_module('1-concurrent_coroutines')

wait_n = concurrent_coroutines.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the avarage runtime."""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
