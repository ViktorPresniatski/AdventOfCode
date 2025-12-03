import utils as ut


def task_1():
    print("------TASK-1------")
    file = ut.read()

    res = 0
    for line in file:
        bank = list(map(int, line))
        cur_res = -1
        prev_max = bank[-1]

        for i in range(len(bank) - 2, -1, -1):
            num = bank[i]
            cur_res = max(10 * num + prev_max, cur_res)
            prev_max = max(num, prev_max)

        res += cur_res

    return res


def task_2():
    print("------TASK-2------")
    file = ut.read()
    res = 0
    num_to_select = 12

    for line in file:
        bank = [int(ch) for ch in line]
        n = len(bank)

        result = []
        start_idx = 0

        for i in range(num_to_select):
            end_idx = n - num_to_select + i

            max_digit = -1
            max_idx = start_idx
            for j in range(start_idx, end_idx + 1):
                if bank[j] > max_digit:
                    max_digit = bank[j]
                    max_idx = j

            result.append(max_digit)
            start_idx = max_idx + 1

        joltage = int(''.join(map(str, result)))
        res += joltage

    return res
