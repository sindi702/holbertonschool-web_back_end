#!/usr/bin/env python3
'''async file'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' async generator '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
