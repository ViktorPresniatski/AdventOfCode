import numpy as np
import utils as ut


def task_1():
    print("------TASK-1------")
    file = ut.read()
    
    ranges = [list(map(int, f.split('-'))) for f in file[0].split(',')]

    res = 0
    for r in ranges:
        for i in range(r[0], r[1] + 1):
            i_str = str(i)
            pivot = len(i_str) // 2
            # print(i_str, i_str[:pivot], i_str[pivot:])
            if i_str[:pivot] == i_str[pivot:]:
                res += i
    return res
    

def task_2():
    print("------TASK-2------")
    file = ut.read()
        
    ranges = [list(map(int, f.split('-'))) for f in file[0].split(',')]
    used = set()

    for r in ranges:
        for id_num in range(r[0], r[1] + 1):
            id_str = str(id_num)
            
            for option in range(2, len(id_str) + 1):
                if len(id_str) % option != 0: continue

                pivot = len(id_str) // option
                cur = pivot
                while id_str[cur - pivot:cur] == id_str[cur:cur + pivot]:
                    cur += pivot
                    if cur >= len(id_str):
                        # Found invalid ID
                        used.add(id_num)

    return sum(used)
