import functools
import utils as ut


def compare(first, second):
    if isinstance(first, list) and isinstance(second, list):
        for i in range(max(len(first), len(second))):
            if i >= len(first):
                return -1
            if i >= len(second):
                return 1
            left = first[i]
            right = second[i]
            ans = compare(left, right)
            if ans:
                return ans
    elif isinstance(first, int) and isinstance(second, int):
        if first < second:
            return -1
        if first > second:
            return 1
    elif isinstance(first, list) or isinstance(second, int):
        second = [second]
        return compare(first, second)
    elif isinstance(first, int) or isinstance(second, list):
        first = [first]
        return compare(first, second)
    return 0


def task_1():
    file = ut.read(group=True)
    res = 0
    for ind, group in enumerate(file):
        first, second = group
        first = eval(first)
        second = eval(second)
        ans = compare(first, second)
        if ans == -1:
            res += ind + 1
    return res


def task_2():
    file = ut.read(group=True)
    res = [
        [[2]],
        [[6]],
    ]
    for ind, group in enumerate(file):
        first, second = group
        first = eval(first)
        second = eval(second)
        res.extend([first, second])

    first_ind, second_ind = None, None
    for ind, el in enumerate(sorted(res, key=functools.cmp_to_key(compare))):
        if el == [[2]]:
            first_ind = ind + 1
        if el == [[6]]:
            second_ind = ind + 1

    return first_ind * second_ind
