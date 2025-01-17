#!/usr/bin/env python3
"""A program that uses a measure_time function"""

import asyncio
import random
import time
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int = 10) -> float:
    """
    A function with integers n and max_delay as arguments that measures
    the total execution time for wait_n(n, max_delay), and returns 
    the total_time/n as a float value
    """
    elapsed_time: float

    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time
    return total_time / n
