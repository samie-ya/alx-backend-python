#!/usr/bin/env python3
"""This script will recreate wait_n with task"""

from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """This function will recreate wait_n function"""
    newlist = []
    for i in range(n):
        task1 = task_wait_random(max_delay)
        newlist.append(await task1)
    return sorted(newlist)
