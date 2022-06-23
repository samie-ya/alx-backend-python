#!/usr/bin/env python3
"""This script will return multiplies float with multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This function will return  a function"""
    def func(value: float) -> float:
        """This function will multiply a float with multiplier"""
        return multiplier * value
    return func
