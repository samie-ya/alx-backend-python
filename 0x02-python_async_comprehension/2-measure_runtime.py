#!/usr/bin/env python3
"""This script will measure the time it takes to go through function"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """This function will tell how long it took for a function to finish"""
    start = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = time.time()
    return end - start
