#!/usr/bin/env python3
"""This script will use the ten numbers from async generator"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """This function will return random numbers"""
    newlist = []
    async for i in async_generator():
        newlist.append(i)
    return newlist
