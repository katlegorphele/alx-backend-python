#!/usr/bin/env python3

"""
Given the parameters and the return values, add type annotations to
the function def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default

"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar("T")
NoneType = TypeVar("NoneType", None, None)
R = Union[Any, T]
D = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: D) -> R:
    """
    Returns a value from a dictionary or the default
    """
    if key in dct:
        return dct[key]
    else:
        return default
