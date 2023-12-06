import math

import utils as ut


def solve(times, dist):
    ans = 1
    for i in range(len(times)):
        x = times[i]
        d = dist[i]
        first = (x - math.sqrt(x ** 2 - 4 * d)) // 2 + 1
        second = (x + math.sqrt(x ** 2 - 4 * d)) / 2
        if second.is_integer():
            second -= 1
        ans *= int(second) - int(first) + 1
    return ans


def task_1():
    file = ut.read()
    times = list(map(int, filter(None, file[0].replace('Time: ', '').strip().split(' '))))
    dist = list(map(int, filter(None, file[1].replace('Distance: ', '').strip().split(' '))))

    return solve(times, dist)


def task_2():
    file = ut.read()
    times = filter(None, file[0].replace('Time: ', '').strip().split(' '))
    dist = filter(None, file[1].replace('Distance: ', '').strip().split(' '))
    times = int(''.join(times))
    dist = int(''.join(dist))
    return solve([times], [dist])
