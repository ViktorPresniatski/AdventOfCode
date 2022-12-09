import numpy as np
import utils as ut


def visible(arr, pos_i, pos_j):
    pivot = arr[pos_i][pos_j]

    return arr[pos_i, :pos_j].max() < pivot or \
            arr[pos_i, pos_j + 1:].max() < pivot or \
            arr[:pos_i, pos_j].max() < pivot or \
            arr[pos_i + 1:, pos_j].max() < pivot


def task_1():
    file = ut.read()
    arr = np.array([[int(el) for el in row] for row in file])
    total_score = 0
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[0]) - 1):
            total_score += int(visible(arr, i, j))
    total_score += len(arr[0]) * 4 - 4
    return total_score


def calc_score(arr, pos_i, pos_j):
    w, h = len(arr[0]), len(arr)
    pivot = arr[pos_i][pos_j]

    i, j = pos_i, pos_j
    while i > 0:
        i -= 1
        if arr[i][pos_j] >= pivot:
            break
    u = pos_i - i

    i, j = pos_i, pos_j
    while i < h - 1:
        i += 1
        if arr[i][pos_j] >= pivot:
            break
    d = i - pos_i

    i, j = pos_i, pos_j
    while j > 0:
        j -= 1
        if arr[pos_i][j] >= pivot:
            break
    l = pos_j - j

    i, j = pos_i, pos_j
    while j < w - 1:
        j += 1
        if arr[pos_i][j] >= pivot:
            break
    r = j - pos_j

    return l * r * u * d


def task_2():
    file = ut.read()
    arr = np.array([[int(el) for el in row] for row in file])
    max_score = 0
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[0]) - 1):
            score = calc_score(arr, i, j)
            if score > max_score:
                max_score = score
    return max_score


def bad_solution_of_task_1():
    def rotated(array_2d):
        list_of_tuples = zip(*array_2d[::-1])
        return [list(elem) for elem in list_of_tuples]

    def calc_total(file, matr):
        total = 0
        for row, f in enumerate(file[1:-1]):
            f = list(map(int, f))
            i = 1
            max_in_row = f[0]
            max_pos = 0
            while i < len(f):
                if f[i] > max_in_row:
                    max_in_row = f[i]
                    max_pos = i
                    if not matr[row + 1][i]:
                        total += 1
                        matr[row + 1][i] = 1
                i += 1
            if max_pos == len(f) - 1:
                break
            j = len(f) - 1 - 1
            max_in_row = f[len(f) - 1]
            while j > max_pos:
                if f[j] > max_in_row:
                    max_in_row = f[j]
                    if not matr[row + 1][j]:
                        total += 1
                        matr[row + 1][j] = 1
                j -= 1
        return total

    total = 0
    file = ut.read()
    matr = [[0 for _ in range(len(file[0]))] for f in range(len(file) - 2)]
    for m in matr:
        m[0] = 1
        m[-1] = 1
    matr.insert(0, [1 for _ in range(len(file[0]))])
    matr.append([1 for _ in range(len(file[0]))])

    total += calc_total(file, matr)
    total += calc_total(rotated(file), rotated(matr))
    total += len(file[0]) * 4 - 4

    return total
