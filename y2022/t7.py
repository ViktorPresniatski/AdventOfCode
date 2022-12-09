import os
from collections import defaultdict

import utils as ut


def cd_dir(cur_dir, next_dir):
    return f'{cur_dir}{next_dir}/'


def build_filesystem(file):
    G = defaultdict(list)
    cur_dir = '/'
    i = 1
    while i < len(file):
        if file[i] == '$ ls':
            while True:
                i += 1
                if i >= len(file) or file[i].startswith('$'):
                    break
                a, b = file[i].split()
                if a == 'dir':
                    G[cur_dir].append([cd_dir(cur_dir, b)])
                else:
                    G[cur_dir].append((b, int(a)))
        elif file[i].startswith('$ cd'):
            cd = file[i].split()[-1]
            if cd == '..':
                prev_dir = os.path.dirname(cur_dir.rstrip('/'))
                if prev_dir != '/':
                    prev_dir += '/'
                cur_dir = prev_dir
            else:
                next_dir = f'{cur_dir}{cd}/'
                cur_dir = next_dir
            i += 1
    return G


def calc_size(G, cur_dir='/', res=None):
    size = 0
    for ne in G[cur_dir]:
        if len(ne) == 1:
            size += calc_size(G, ne[0], res=res)
        else:
            size += ne[1]
    res[cur_dir] = size
    return size


def task_1():
    file = ut.read()
    G = build_filesystem(file)

    res = defaultdict(int)
    calc_size(G, res=res)
    total = 0
    for k, v in res.items():
        if v <= 100000:
            total += v
    return total


def task_2():
    file = ut.read()
    G = build_filesystem(file)

    res = defaultdict(int)
    total_size = calc_size(G, res=res)

    delta = total_size - 40000000

    min_value = float('inf')
    for k, v in res.items():
        if v >= delta and v < min_value:
            min_value = v
    return min_value
