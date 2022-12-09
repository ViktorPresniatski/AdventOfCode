import utils as ut


score_mapping = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}
win_mapping = {
    1: 3,
    2: 1,
    3: 2,
}


def _calc_score(first, second):
    f, s = score_mapping[first], score_mapping[second]

    if f == s:
        return s + 3
    if win_mapping[s] == f:
        return s + 6
    return s + 0


def task_1():
    total_score = 0
    lines = ut.read()
    for line in lines:
        a, x = line.split()
        total_score += _calc_score(a, x)

    return total_score


reverse_win_mapping = {
    3: 1,
    1: 2,
    2: 3,
}


def _calc_score_right(first, result):
    f = score_mapping[first]

    if result == 'Y':
        return f + 3
    if result == 'X':
        return win_mapping[f] + 0
    if result == 'Z':
        return reverse_win_mapping[f] + 6
    raise Exception('Oooops: %s %s', first, result)


def task_2():
    total_score = 0
    lines = ut.read()
    for line in lines:
        a, x = line.split()
        total_score += _calc_score_right(a, x)

    return total_score
