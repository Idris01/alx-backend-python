#!/usr/bin/env python3
"""This module define a function that takes a float and return a function
"""
from typing import Callable

ReturnFunc = Callable[[float], float]


def make_multiplier(multiplier: float) -> ReturnFunc:
    """Takes a multiplier and return a function
    that takes a numner to multiply it
    """

    return lambda num: num * multiplier
