import functools
import utils as ut


def is_bad(sets, constraints):
    for s in sets:
        cubes = s.split(', ')
        for c in cubes:
            num, color = c.split(' ')
            if int(num) > constraints[color]:
                return True



def task_1():
    constr = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    file = ut.read()
    res = []
    for line in file:
        game, sets = line.split(': ')
        g_id = int(game.replace('Game ', ''))
        sets = sets.split('; ')

        if not is_bad(sets, constr):
            res.append(g_id)

    return sum(res)


def find_prod(sets):
    expected = {
        'red': [],
        'green': [],
        'blue': [],
    }
    for s in sets:
        cubes = s.split(', ')
        for c in cubes:
            num, color = c.split(' ')
            expected[color].append(int(num))
    return functools.reduce(lambda x, y: x * max(y), expected.values(), 1)


def task_2():
    file = ut.read()
    res = 0
    for line in file:
        _, sets = line.split(': ')
        sets = sets.split('; ')
        res += find_prod(sets)
    return res
