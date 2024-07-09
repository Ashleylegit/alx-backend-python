#!/usr/bin/env python3
"""An asynchronous coroutine"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    A function that receives an integer value, waits for a random 
    number of seconds before returning the integer value
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
