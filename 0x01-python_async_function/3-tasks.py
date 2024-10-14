#!/usr/bin/env python3
"""function that takes an integer and returns a task"""


import asyncio
import importlib

basic_async_syntax = importlib.import_module('0-basic_async_syntax')
wait_random = basic_async_syntax.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an asyncio task that waits for a random delay."""
    return asyncio.create_task(wait_random(max_delay))
