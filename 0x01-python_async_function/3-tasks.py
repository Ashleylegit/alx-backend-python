#!/usr/bin/env python3
"""A function task_wait_random"""

import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    A function task_wait_random that takes an integer max_delay and returns
    a asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
