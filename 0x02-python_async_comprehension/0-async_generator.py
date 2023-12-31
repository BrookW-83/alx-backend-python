#!/usr/bin/env python3
'''Async Generator module.'''

import asyncio #implement async 
import random
from typing import Generator

'''
implement Generates a sequence of 10 numbers.
'''
async def async_generator() -> Generator[float, None, None]:
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)