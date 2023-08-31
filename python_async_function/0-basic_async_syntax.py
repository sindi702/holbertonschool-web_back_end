#!/usr/bin/env python3
''' documentation'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''wait randin func'''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
