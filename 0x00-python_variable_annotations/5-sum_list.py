#!/usr/bin/env python3
"""This script will give the sum of float"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """This function wil return the sum of float"""
    add: float = 0.0
    for value in input_list:
        add += value
    return add
