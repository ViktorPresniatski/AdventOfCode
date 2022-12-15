import re
import numpy as np
import utils as ut


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def read_cords():
    file = ut.read()
    cords = []
    beacons = set()
    for f in file:
        match = re.match('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', f)
        s_x, s_y, b_x, b_y = map(int, match.groups())
        beacons.add((b_x, b_y))
        d = manhattan([s_x, s_y], [b_x, b_y])
        cords.append([(s_x, s_y), (b_x, b_y), d])

    return cords, beacons


def calc_segments_on_x_axis(y, cords, min_x=-np.inf, max_x=np.inf):
    segments = []
    for s, b, d in cords:
        d_y = abs(s[1] - y)
        if d_y > d:
            continue
        delta = d - d_y

        left, right = max(s[0] - delta, min_x), min(s[0] + delta, max_x)
        if left > right:
            continue
        left, right = s[0] - delta, s[0] + delta
        segments.append((left, right))

    segments.sort()
    return segments


def unite_segments(first, second):
    return min(first[0], second[0]), max(first[1], second[1])


def task_1():
    cords, beacons = read_cords()
    y = 2_000_000
    segments = calc_segments_on_x_axis(y, cords)
    max_line = segments[0]
    for left, right in segments[1:]:
        assert left <= max_line[1] + 1
        max_line = unite_segments(max_line, (left, right))

    result = max_line[1] - max_line[0] + 1
    return result - sum(1 for b in beacons if b[1] == y and max_line[0] <= b[0] <= max_line[1])


def task_2():
    MIN_X, MAX_X = 0, 4_000_000
    cords, _ = read_cords()

    for y in range(MAX_X + 1):
        segments = calc_segments_on_x_axis(y, cords, min_x=MIN_X, max_x=MAX_X)
        max_line = (0, 0)
        for left, right in segments:
            if max_line[1] + 1 < left:
                x = max_line[1] + 1
                return x * MAX_X + y
            max_line = unite_segments(max_line, (left, right))
