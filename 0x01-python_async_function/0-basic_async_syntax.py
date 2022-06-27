#!/usr/bin/env python3
"""This script will contain asychoronous coroutine"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """This function will return random wait number from 0 to max_delay"""
    rand: float = random.uniform(0, max_delay)
    time: float = await asyncio.sleep(rand)
    return rand
