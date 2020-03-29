# Simple state machine with coroutines (using async/await)

""" State Diagram

      ============
      |    S0    |
      ============
       |        | 
       1        0
       |        |
       V        V
 ========     ========
 |  S1  |--1->|  S2  |
 |      |<-0--|      |
 ========     ========
   |  ^         |
   0  |         1
   |  0         |
   V  |         V
  =================      ========
  |       S3      |--1-->|  S4  |
  =================      ========
"""

import asyncio
import time

from random import randint


async def start_state():
    print('Start State is called')
    input_value = randint(0, 1)
    time.sleep(1)
    if input_value == 0:
        result = await state2(input_value)
    else:
        result = await state1(input_value)
    print('Resume of the Transition:')
    print(f'Start State calling {result}')


async def state1(transition_value):
    output_value = f'State 1 with transition value = {transition_value}'
    input_value = randint(0, 1)
    time.sleep(1)
    print('...evaluating...')
    if input_value == 0:
        result = await state3(input_value)
    else:
        result = await state2(input_value)
    return '\n'.join([output_value, f'State 1 calling {result}'])


async def state2(transition_value):
    output_value = f'State 2 with transition value = {transition_value}'
    input_value = randint(0, 1)
    time.sleep(1)
    print('...evaluating...')
    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await state3(input_value)
    return '\n'.join([output_value, f'State 2 calling {result}'])


async def state3(transition_value):
    output_value = f'State 3 with transition value = {transition_value}'
    input_value = randint(0, 1)
    time.sleep(1)
    print('...evaluating...')
    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await end_state(input_value)
    return '\n'.join([output_value, f'State 3 calling {result}'])


async def end_state(transition_value):
    output_value = f'State 3 with transition value = {transition_value}'
    print('...stop computation...')
    return output_value


if __name__ == '__main__':
    print('Finite State Machine simulation with Async/Await Coroutine')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_state())
