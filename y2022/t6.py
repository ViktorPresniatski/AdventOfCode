import utils as ut


def task_1():
    file = ut.read()
    text = file[0]
    for i in range(len(text) - 4):
        if len(set(text[i:i + 4])) == 4:
            return i + 4


def task_2():
    file = ut.read()
    text = file[0]
    for i in range(len(text) - 14):
        if len(set(text[i:i + 14])) == 14:
            return i + 14
