#!/usr/bin/env python3
''' Async Comprehensions module.'''
from typing import List # import librayry
from importlib import import_module as using

'''
Creates a list of 10 numbers from a 10-number generator.
'''

async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    
    return [num async for num in async_generator()]