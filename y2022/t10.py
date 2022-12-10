import utils as ut


def task_1():
    file = ut.read()
    output = []
    X = 1
    for f in file:
        if f.startswith('noop'):
            output.append(X)
        else:
            c, val = f.split()
            val = int(val)
            output.append(X)
            output.append(X)
            X += val

    total = 0
    for el in [20, 60, 100, 140, 180, 220]:
        total += el * output[el - 1]
    return total


def draw(middle, cycle):
    return '#' if middle - 1 <= cycle % 40 <= middle + 1 else '.'


def task_2():
    file = ut.read()
    cur_cycle = 0
    output = []
    stripe_middle = 1
    for f in file:
        if f.startswith('noop'):
            output.append(draw(stripe_middle, cur_cycle))
            cur_cycle += 1
        else:
            c, val = f.split()
            val = int(val)
            output.append(draw(stripe_middle, cur_cycle))
            cur_cycle += 1
            output.append(draw(stripe_middle, cur_cycle))
            cur_cycle += 1
            stripe_middle += val

    result = '\n'.join([''.join(batch) for batch in ut.get_batch(output, 40)])
    return result
