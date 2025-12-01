import numpy as np
import utils as ut


def task_1():
    print("------TASK-2------")
    file = ut.read()

    res = 0
    total = 50
    for i in file:
        if i.startswith('L'):
            total -= int(i[1:])
        elif i.startswith('R'):
            total += int(i[1:])
        else:
            raise ValueError(f'What the direction??? {i}')

        if total % 100 == 0:
            res += 1
    return res


def task_2():
    print("------TASK-2------")
    file = ut.read()

    res = 0
    current_val = 50
    for i in file:
        dist = int(i[1:])
        from_zero = current_val == 0
        intermediate = dist // 100
        res += intermediate
        rest = dist % 100

        if i.startswith('L'):
            current_val -= rest
        elif i.startswith('R'):
            current_val += rest
        else:
            raise ValueError(f'What the direction??? {i}')

        if not from_zero and (current_val <= 0 or current_val >= 100):
            res += 1
        current_val %= 100
    return res