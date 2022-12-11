import numpy as np
import utils as ut


def calc_operation(op, old):
    if op == 'old * old':
        return old * old
    elif op.startswith('old + '):
        return old + int(op.replace('old + ', ''))
    elif op.startswith('old * '):
        return old * int(op.replace('old * ', ''))
    else:
        ut.exc('Cannnot parse operation')


def build_M():
    M = []
    file = ut.read(group=True)
    for f in file:
        M.append(
            {
                'items': list(map(int, f[1].replace('  Starting items: ', '').split(', '))),
                'operation': f[2].replace('  Operation: new = ', ''),
                'test': int(f[3].replace('  Test: divisible by ', '')),
                'iftrue': int(f[4].replace('    If true: throw to monkey ', '')),
                'iffalse': int(f[5].replace('    If false: throw to monkey ', '')),
                'num_inspects': 0,
            }
        )
    return M


def run(M, num_rounds, reduce):
    for _ in range(num_rounds):
        for m in M:
            for it in m['items']:
                new = calc_operation(m['operation'], it)
                new = reduce(new)
                if new % m['test'] == 0:
                    M[m['iftrue']]['items'].append(new)
                else:
                    M[m['iffalse']]['items'].append(new)
                m['num_inspects'] += 1
            m['items'] = []

    return np.prod(list(reversed(sorted([m['num_inspects'] for m in M])))[:2])


def task_1():
    M = build_M()
    reduce = lambda x: x // 3
    return run(M, num_rounds=20, reduce=reduce)


def task_2():
    M = build_M()
    denominator = np.prod([m['test'] for m in M])
    reduce = lambda x: x % denominator
    return run(M, num_rounds=10_000, reduce=reduce)
