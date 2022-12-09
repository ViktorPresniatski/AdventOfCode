import utils as ut


def task_1():
    max_sum = 0
    groups = ut.read(t=int, group=True)
    for group in groups:
        cur_sum = sum(group)
        if cur_sum > max_sum:
            max_sum = cur_sum
    return max_sum


def task_2():
    top_three = []
    groups = ut.read(t=int, group=True)
    for group in groups:
        cur_sum = sum(group)
        top_three.append(cur_sum)
        top_three = sorted(top_three)[-3:]
    return sum(top_three)
