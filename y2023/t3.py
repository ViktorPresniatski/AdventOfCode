import utils as ut

adj = [(-1, 0), (1, 0)]
diag_first = [(-1, -1), (0, -1), (1, -1)]
diag_last = [(-1, 1), (0, 1), (1, 1)]


def _is_valid(i, j, arr, first=False, last=False):
    M, N = len(arr), len(arr[0])
    if first:
        sides = diag_first
    elif last:
        sides = diag_last
    else:
        sides = adj

    for dx, dy in sides:
        x, y = i + dx, j + dy
        if not (0 <= x < M) or not (0 <= y < N):
            continue
        if arr[x][y] != '.':
            return True
    return False


def task_1():
    file = ut.read()
    ans = 0
    for i, line in enumerate(file):
        j = -1
        while j < len(line) - 1:
            j += 1
            ch = line[j]
            if not ch.isdigit():
                continue
            buff = []
            valid = _is_valid(i, j, file, first=True)

            while j < len(line) and line[j].isdigit():
                valid = valid or _is_valid(i, j, file)
                buff.append(line[j])
                j += 1
            valid = valid or _is_valid(i, j - 1, file, last=True)
            if not valid:
                continue
            ans += int(''.join(buff))
    return ans


def _find_adj_numbers(orig_i, orig_j, arr):
    res = []

    def go_left(cur_i, cur_j):
        buff = []
        if cur_j - 1 >= 0 and arr[cur_i][cur_j - 1].isdigit():
            j = cur_j - 1
            while j >= 0 and arr[cur_i][j].isdigit():
                buff.append(arr[cur_i][j])
                j -= 1
            num = int(''.join(list(reversed(buff))))
            res.append(num)

    def go_right(cur_i, cur_j):
        buff = []
        if cur_j + 1 < len(arr[0]) and arr[cur_i][cur_j + 1].isdigit():
            j = cur_j + 1
            while j < len(arr[0]) and arr[cur_i][j].isdigit():
                buff.append(arr[cur_i][j])
                j += 1
            num = int(''.join(buff))
            res.append(num)

    def go_left_and_right(i, j):
        go_left(i, j)
        go_right(i, j)

    def go_from_the_middle(i, j):
        while j >= 0 and arr[i][j].isdigit():
            j -= 1
        go_right(i, j)


    go_left_and_right(orig_i, orig_j)

    if orig_i - 1 >= 0:
        if not arr[orig_i - 1][orig_j].isdigit():
            go_left_and_right(orig_i - 1, orig_j)
        else:
            go_from_the_middle(orig_i - 1, orig_j)

    if orig_i + 1 < len(arr):
        if not arr[orig_i + 1][orig_j].isdigit():
            go_left_and_right(orig_i + 1, orig_j)
        else:
            go_from_the_middle(orig_i + 1, orig_j)

    return res


def task_2():
    file = ut.read()
    ans = 0
    for i, line in enumerate(file):
        for j, ch in enumerate(line):
            if ch == '*':
                nums = _find_adj_numbers(i, j, file)
                if len(nums) == 2:
                    ans += nums[0] * nums[1]
    return ans
