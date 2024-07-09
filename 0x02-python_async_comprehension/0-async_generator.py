#!/usr/bin/env python3
"""A coroutine called async_generator"""

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """
    A function that loops 10 times yielding a random number between
    0 and 10
    """
    for i in range(10):
        yield random.random() * 10
        await asyncio.sleep(1)
