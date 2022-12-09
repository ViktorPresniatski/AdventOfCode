import utils as ut


def task_1():
    inputs = ut.read()
    res = 0
    for i in inputs:
        el1, el2 = i.split(',')
        begin, end = el1.split('-')
        set1 = set(range(int(begin), int(end) + 1))
        begin, end = el2.split('-')
        set2 = set(range(int(begin), int(end) + 1))
        intersect = set1 & set2
        if intersect == set1 or intersect == set2:
            res += 1
    return res


def task_2():
    inputs = ut.read()
    res = 0
    for i in inputs:
        el1, el2 = i.split(',')
        begin, end = el1.split('-')
        set1 = set(range(int(begin), int(end) + 1))
        begin, end = el2.split('-')
        set2 = set(range(int(begin), int(end) + 1))
        intersect = set1 & set2
        if intersect:
            res += 1
    return res
