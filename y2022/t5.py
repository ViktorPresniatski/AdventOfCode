import utils as ut


def get_stacks(file):
    S = [[] for _ in range(9)]
    for line in file[:8]:
        for i in range(1, 36, 4):
            S[i // 4].append(line[i])
    return [list([el for el in reversed(s) if el != ' ']) for s in S]


def parse_line(line):
    __, _ = line.split('move ')
    move, _ = _.split(' from ')
    fro, to = _.split(' to ')
    return int(move), int(fro), int(to)


def task_1():
    file = ut.read()
    S = get_stacks(file)

    for line in file[10:]:
        m, f, t = parse_line(line)
        for _ in range(m):
            el = S[f - 1].pop()
            S[t - 1].append(el)

    res = ''.join([s[-1] for s in S])
    return res


def task_2():
    file = ut.read()
    S = get_stacks(file)
    file = file[10:]
    for line in file:
        m, f, t = parse_line(line)
        els = []
        for _ in range(m):
            els.append(S[f - 1].pop())
        S[t - 1].extend(list(reversed(els)))

    res = ''.join([s[-1] for s in S])
    return res
