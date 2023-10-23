#!/usr/bin/env python3

from typing import Union, Tuple

"""
Function that returns a tuple with a string and a float.
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and a float
    """
    return (k, v**2)
