#!/usr/bin/env python3
"""This script requires mypy clean up"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """This function will take a tuple and int to give a list"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
