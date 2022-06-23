#!/usr/bin/env python3
"""This script will do duck typing"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]):
    """This function will annotate parameters and return values"""
    return [(i, len(i)) for i in lst]
