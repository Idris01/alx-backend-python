#!/usr/bin/env python3
"""This module define a function that return first element of a list
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first item in a sequence

    Arguments:
    =========
    lst (sequence)- sequence of any type

    Returns - first item or None if lst is empty
    """
    if lst:
        return lst[0]
    else:
        return None
