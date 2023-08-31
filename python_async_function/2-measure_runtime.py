#!/usr/bin/env python3
''' documentation'''
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''messure time wait_n'''
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    elapse_time = end_time - start_time
    return elapse_time / n
