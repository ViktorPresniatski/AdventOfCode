import utils as ut

INPUT_FILE = 'data/input1.3.txt'
from collections import Counter


def task_1():
    file = ut.read()
    res = ''
    res2 = ''
    for i in range(len(file[0])):
        c = Counter([f[i] for f in file])
        res += c.most_common()[0][0]
        res2 += c.most_common()[1][0]
    return int(res, 2) * int(res2, 2)


def calc_score(file, default=0):
    res = file.copy()
    default_str = '0' if default else '1'
    for i in range(len(file[0])):
        res_list = []
        c = Counter([f[i] for f in res])
        com = c.most_common()
        if com[0][1] == com[1][1]:
            com = default_str
        else:
            com = com[default][0]
        for f in res:
            if f[i] == com:
                res_list.append(f)
        res = res_list
        if len(res) == 1:
            break
    return int(res[0], 2)


def task_2():
    file = ut.read()
    a = calc_score(file, default=0)
    b = calc_score(file, default=1)
    return a * b


if __name__ == '__main__':
    ut.main()
