import numpy as np
import utils as ut


def task_1():
    file = ut.read()
    ans = 0
    for line in file:
        _, nums = line.split(': ')
        left, right = nums.split(' | ')
        left = set([l.strip() for l in left.split(' ') if l.strip()])
        right = set([r.strip() for r in right.split(' ') if r.strip()])
        exp = len(left & right)
        if exp:
            ans += 2**(exp - 1)
    return ans

def task_2():
    file = ut.read()
    ans = 0
    arr = []
    for line in file:
        _, nums = line.split(': ')
        left, right = nums.split(' | ')
        left = set([l.strip() for l in left.split(' ') if l.strip()])
        right = set([r.strip() for r in right.split(' ') if r.strip()])
        exp = len(left & right)
        arr.append(exp)

    N = len(arr)
    #
    # q = []
    # for i, res in enumerate(arr):
    #     end = min(i + res + 1, N)
    #     q.extend([j for j in range(i + 1, end)])
    #
    # ans = N
    # # q = [q_i for q_i in q if q_i < N]
    # print(q)
    # while q:
    #     ans += 1
    #     i = q.pop(0)
    #     res = arr[i]
    #     end = min(i + res + 1, N)
    #     q.extend([j for j in range(i + 1, end)])
    #     print(i, [j for j in range(i + 1, end)])
    # return ans
    exps = [1] * N
    for i in range(N):
        for j in range(arr[i]):
            exps[i + j + 1] += exps[i]
    return sum(exps)

