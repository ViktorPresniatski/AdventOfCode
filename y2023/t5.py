import utils as ut


def _convert_to_arr(file):
    return [[list(map(int, line.split(' '))) for line in group[1:]] for group in file[1:]]


def _find_next(seed, mapp):
    for r in mapp:
        if r[1] <= seed < r[1] + r[2]:
            return r[0] + (seed - r[1])
    return seed


def task_1():
    file = ut.read(group=True)
    seeds = [int(item) for item in file[0][0].replace('seeds: ', '').split(' ')]
    arr = _convert_to_arr(file)
    ans = float('inf')
    for seed in seeds:
        nxt = seed
        for group in arr:
            nxt = _find_next(nxt, group)

        ans = min(ans, nxt)
    return ans


def _find_new_lines(cur_seed, group):
    res = []
    print(f'Cur seed: [{cur_seed[0]}, {cur_seed[1]}]')
    last = cur_seed[0]
    for r in group:
        print(f'[{r[1]}, {r[1] + r[2] - 1}]', f'-> [{r[0]}, {r[0] + r[2] - 1}]')
        src, dst, le = r[1], r[0], r[2]
        left, right = max(cur_seed[0], src), min(cur_seed[1], src + le - 1)
        if left <= right:
            if last < left:
                res.append((last, left - 1))
            last = right + 1
            res.append((dst - src + left, dst - src + right))
    if last <= cur_seed[1]:
        res.append((last, cur_seed[1]))

    return res


def task_2():
    file = ut.read(group=True)
    seeds = [int(item) for item in file[0][0].replace('seeds: ', '').split(' ')]
    arr = [sorted([list(map(int, line.split(' '))) for line in group[1:]], key=lambda x: x[1]) for group in file[1:]]

    lines = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]
    lines.sort()

    for group in arr:
        nxt_lines = []
        # print(lines)
        for i in range(len(lines)):
            cur_seed = lines[i]
            new_lines = _find_new_lines(cur_seed, group)
            print(f'New lines: {new_lines}', end='\n\n')
            nxt_lines.extend(new_lines)
        lines = nxt_lines
        print('---------------------------------------')

    ans = min([l[0] for l in lines])

    return ans
