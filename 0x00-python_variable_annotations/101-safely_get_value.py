#!/usr/bin/env python3
"""This module define a function that safely get a given key from a dictionary
"""
from typing import Union, Mapping, TypeVar, Any

T = TypeVar("T")


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """Returnbthe value corresponding to key if key is in dct
    Return default value if key not found
    """
    if key in dct:
        return dct[key]
    else:
        return default
