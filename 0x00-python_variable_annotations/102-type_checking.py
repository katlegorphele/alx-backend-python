#!/usr/bin/env python3
from typing import List, Union
'''
Using mypy to validate the following piece of code and apply any necessary changes.
'''

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Returns the sum of a list of floats
    '''
    return sum(mxd_lst)