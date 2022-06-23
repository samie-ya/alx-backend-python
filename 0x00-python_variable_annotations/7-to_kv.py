#!/usr/bin/env python3
"""This script will create tuple from argument"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This function will return tuple from the argument"""
    tup: tuple = (str(k), v**2)
    return tup
