#!/usr/bin/env python3
"""This script will handle tasks"""

import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Any:
    """This function will return asyncio task"""
    return asyncio.create_task(wait_random(max_delay))
