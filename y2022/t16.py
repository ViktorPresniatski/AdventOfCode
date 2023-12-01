import re
import numpy as np
import utils as ut


def task_1():
    file = ut.read()
    for f in file:
        match = re.match('Valve (\w+) has flow rate=(\d+); tunnels lead to valves (.+)')
        v, r, next_v = match.groups()
        next_v = next_v.split(', ')




def task_2():
    file = ut.read()
