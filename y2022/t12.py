import numpy as np
import utils as ut
from collections import deque


def find(symbol, arr):
    h, w = arr.shape
    res = []
    for i in range(h):
        for j in range(w):
            if arr[i, j] == symbol:
                res.append((i, j))
    return res


def can_step(cur, next):
    if cur == 'S':
        cur = 'a'
    if next == 'E':
        next = 'z'
    return ord(next) - ord(cur) <= 1


def bfs(arr, starts):
    h, w = arr.shape
    q = deque(starts)
    visited = set(starts)
    costs = np.full((h, w), 1_000_000)
    for s in starts:
        costs[s] = 0

    while len(q):
        cur = q.popleft()
        if arr[cur] == 'E':
            break
        for step in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_pos = cur[0] + step[0], cur[1] + step[1]
            if not (next_pos[0] >= 0 and next_pos[0] < h and next_pos[1] >= 0 and next_pos[1] < w):
                continue
            if next_pos in visited:
                continue
            if not can_step(arr[cur], arr[next_pos]):
                continue
            if costs[cur] + 1 < costs[next_pos]:
                q.append(next_pos)
                visited.add(next_pos)
                costs[next_pos] = costs[cur] + 1

    return costs


def task_1():
    arr = ut.read_matrix()
    starts = find('S', arr)
    end_pos = find('E', arr)[0]
    costs = bfs(arr, starts)
    return costs[end_pos]


def task_2():
    arr = ut.read_matrix()
    starts = find('a', arr) + find('S', arr)
    end_pos = find('E', arr)[0]
    costs = bfs(arr, starts)
    return costs[end_pos]
