import sys

year = sys.argv[1]
task_number = sys.argv[2]

body = f"""import numpy as np
import utils as ut


def task_1():
    file = ut.read()


def task_2():
    file = ut.read()
"""

with open(f'y{year}/t{task_number}.py', 'w') as f:
    f.write(body)

with open(f'y{year}/data/input{task_number}.txt', 'w') as f:
    pass
