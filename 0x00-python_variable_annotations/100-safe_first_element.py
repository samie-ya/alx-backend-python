#!/usr/bin/env python3
"""This script will assign the proper annontation"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """This function will take a sequence and return the first value"""
    if lst:
        return lst[0]
    else:
        return None
