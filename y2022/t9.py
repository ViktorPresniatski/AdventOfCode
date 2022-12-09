import utils as ut
import numpy as np


def step(positions, d=None):
    head_of_rope = positions[0]

    if d == 'L':
        head_of_rope[1] -= 1
    if d == 'R':
        head_of_rope[1] += 1
    if d == 'U':
        head_of_rope[0] -= 1
    if d == 'D':
        head_of_rope[0] += 1

    for i in range(1, len(positions)):
        pos_head = positions[i - 1]
        pos_tail = positions[i]
        diff_y = pos_head[0] - pos_tail[0]
        diff_x = pos_head[1] - pos_tail[1]

        if np.abs(diff_x) > 1 or np.abs(diff_y) > 1:
            pos_tail[0] += diff_y // np.abs(diff_y) if diff_y else 0
            pos_tail[1] += diff_x // np.abs(diff_x) if diff_x else 0


def run(num_of_knots):
    file = ut.read()
    positions = [[0, 0] for _ in range(num_of_knots)]
    visited = [tuple(positions[-1])]
    for f in file:
        d, val = f.split()
        val = int(val)
        for _ in range(val):
            step(positions, d)
            visited.append(tuple(positions[-1]))

    return len(set(visited))


def task_1():
    return run(2)


def task_2():
    return run(10)
