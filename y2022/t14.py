import numpy as np
import utils as ut


INIT_SOURCE = (0, 500)


def read_map(with_floor=False):
    file = ut.read()
    all_cords = []
    max_y = 0
    for line in file:
        cords = [tuple(map(int, c.split(','))) for c in line.split(' -> ')]
        mb_max_y = max([c[1] for c in cords])
        all_cords.append(cords)
        if mb_max_y > max_y:
            max_y = mb_max_y

    boundaries = (max_y + 3, 1000)
    M = np.zeros(boundaries)

    for cords in all_cords:
        prev_c = cords[0]
        for c in cords[1:]:
            if c[1] < prev_c[1]:
                M[c[1]:prev_c[1] + 1, c[0]] = 1
            elif c[1] > prev_c[1]:
                M[prev_c[1]:c[1] + 1, c[0]] = 1
            elif c[0] < prev_c[0]:
                M[c[1], c[0]:prev_c[0] + 1] = 1
            elif c[0] > prev_c[0]:
                M[c[1], prev_c[0]:c[0] + 1] = 1
            prev_c = c

    if with_floor:
        M[-1, :boundaries[1]] = 1
    return M


def move_sand(M, source):
    next = (source[0] + 1, source[1])
    if not M[next]:
        return next
    next = (source[0] + 1, source[1] - 1)
    if not M[next]:
        return next
    next = (source[0] + 1, source[1] + 1)
    if not M[next]:
        return next
    M[source] = -1
    return INIT_SOURCE


def task_1():
    M = read_map()
    depth = M.shape[0]

    source = INIT_SOURCE
    while source[0] < depth - 1:
        source = move_sand(M, source)

    return np.count_nonzero(M == -1)


def task_2():
    M = read_map(with_floor=True)

    source = INIT_SOURCE
    while M[INIT_SOURCE] != -1:
        source = move_sand(M, source)

    return np.count_nonzero(M == -1)
