#!/usr/bin/env python3
'''documentaion'''

from typing import Union, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''from element to tuple'''
    sec_element = v ** 2
    return (k, sec_element)
