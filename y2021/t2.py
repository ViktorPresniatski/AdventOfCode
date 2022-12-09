import utils as ut

INPUT_FILE = 'data/input1.2.txt'


def task_1():
    file = ut.read()
    hor, dep = 0, 0
    for f in file:
        c, n = f.split()
        n = int(n)
        if c == 'forward':
            hor += n
        if c == 'up':
            dep -= n
        if c == 'down':
            dep += n
    return hor * dep



def task_2():
    file = ut.read()
    hor, dep = 0, 0
    aim = 0
    for f in file:
        c, n = f.split()
        n = int(n)
        if c == 'forward':
            hor += n
            dep += aim * n
        if c == 'up':
            aim -= n
        if c == 'down':
            aim += n
    return hor * dep

if __name__ == '__main__':
    ut.main()
