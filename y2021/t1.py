import utils as ut

INPUT_FILE = 'data/input1.1.txt'


def task_1():
    file = ut.read(int)
    total = 0
    for n in range(1, len(file)):
        if file[n - 1] < file[n]:
            total += 1
    return total

def task_2():
    file = ut.read(int)
    total = 0
    for n in range(1, len(file)):
        if sum(file[n - 1:n + 2]) < sum(file[n:n +3]):
            total += 1
    return total


if __name__ == '__main__':
    ut.main()
