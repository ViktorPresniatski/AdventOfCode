import utils as ut


def task_1():
    file = ut.read()
    sum_ = 0
    for line in file:
        numbers = []
        for el in line:
            if el.isdigit():
                numbers.append(int(el))
        res = 10 * numbers[0] + numbers[-1]
        sum_ += res
    return sum_


num_str = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def _find(word):
    for s in num_str:
        if s in word:
            return num_str[s]


def task_2():
    file = ut.read()
    sum_ = 0
    for line in file:
        numbers = []
        word = ''
        for el in line:
            if el.isdigit():
                numbers.append(int(el))
                continue
            word += el
            res = _find(word)
            if res:
                numbers.append(res)
                word = word[-1]
        res = 10 * numbers[0] + numbers[-1]
        sum_ += res
    return sum_
