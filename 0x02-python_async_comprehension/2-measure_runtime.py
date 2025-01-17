#!/usr/bin/env python3
"""A measure_runtime coroutine"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """A function that measures the total runtime of async_comprehension"""
    start = time.perf_counter()
    coroutines = (async_comprehension() for i in range(4))
    await asyncio.gather(*coroutines)
    end = time.perf_counter()
    return (end - start)
