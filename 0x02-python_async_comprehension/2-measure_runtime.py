#!/usr/bin/env python3
'''Run time for four parallel comprehensions module.'''
import asyncio #implementing asynico
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension

'''
 Executes async_comprehension 4 times and measures the total execution time.
    
'''

async def measure_runtime() -> float:
   
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time