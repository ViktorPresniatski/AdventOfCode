import utils as ut


def find_common_item(left, right):
    for i in left:
        for j in right:
            if i == j:
                return i
    print(left, ' ', right)
    ut.exc('Not found common')


def calc_score(val):
    if 'a' <= val <= 'z':
        return ord(val) - 96
    if 'A' <= val <= 'Z':
        return ord(val) - 38


def task_1():
    total_score = 0
    rucksacks = ut.read()
    for ruck in rucksacks:
        n = len(ruck)
        if n % 2 != 0:
            ut.exc('Ooops not mod 2')
        pivot = n // 2
        left, right = ruck[:pivot], ruck[pivot:]
        common = find_common_item(left, right)
        total_score += calc_score(common)
    return total_score


def find_common_item_out_of_three(first, second, third):
    for i in first:
        for j in second:
            for y in third:
                if i == j == y:
                    return i
    print(first, second, third)
    ut.exc('Not found common item')


def task_2():
    total_score = 0
    rucksacks = ut.read()
    for group in ut.get_batch(rucksacks, 3):
        common = find_common_item_out_of_three(*group)
        total_score += calc_score(common)
    return total_score
