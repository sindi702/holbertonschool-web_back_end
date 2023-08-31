#!/usr/bin/env python3
''' documentation'''
import time
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''same as 1-concurrent but call func '''
    value_list: List[float] = []
    all_list: List[float] = []

    for i in range(n):
        value_list.append(task_wait_random(max_delay))
    for task in asyncio.as_completed(value_list):
        result = await task
        all_list.append(result)
    return all_list
