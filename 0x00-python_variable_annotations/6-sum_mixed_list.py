#!/usr/bin/env python3
"""This script will add content of a list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This function will return sum of list"""
    add: float = 0.0
    for val in mxd_lst:
        add += val
    return add
