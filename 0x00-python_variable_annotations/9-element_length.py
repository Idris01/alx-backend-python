#!/usr/bin/env python3
""" This module define a function that accept a list and return list and
return  new list of tuples of each item in the original list and lenght
of the item
"""
from typing import Sequence, Tuple, Iterable, List

ReturnType = List[Tuple[Sequence, int]]


def element_length(lst: Iterable[Sequence]) -> ReturnType:
    """Take an iterable of sequence and return List of tuple of each item and
    its length
    """
    return [(i, len(i)) for i in lst]
