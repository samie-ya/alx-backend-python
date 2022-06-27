#!/usr/bin/env python3
"""This script will deal with multiple coroutines"""

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """This function will execute multiple coroutes"""
    newlist = []
    for i in range(n):
        rand = await wait_random(max_delay)
        newlist.append(rand)
    return sorted(newlist)
