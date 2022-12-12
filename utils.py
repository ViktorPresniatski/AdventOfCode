import inspect
import numpy as np
from pathlib import Path


def get_input_file():
    prev_exec_func = inspect.stack()[2][0]
    cur_module = inspect.getmodule(prev_exec_func)
    cur_path = Path(cur_module.__file__)
    task_number = cur_path.stem.lstrip('t')
    return Path(cur_module.__file__).parent / 'data' / f'input{task_number}.txt'


def read_file(filename):
    return open(filename).read()


def read(t=str, group=False):
    input_file = get_input_file()
    text = read_file(input_file)
    if group:
        return list(map(lambda a: list(map(t, a.split('\n'))), text.split('\n\n')))
    return list(map(t, text.split('\n')))


def read_matrix(t=str):
    input_file = get_input_file()
    text = read_file(input_file)
    return np.array([[t(el) for el in row] for row in text.split('\n')])


def get_batch(items, max_count):
    for i in range(0, len(items), max_count):
        yield items[i:i + max_count]


def exc(message='Ooops'):
    raise Exception(message)


# def main():
#     module = get_cur_module()
#     try:
#         num = sys.argv[1]
#         result = getattr(module, f'task_{num}')()
#         print(result)
#     except IndexError:
#         print(module.task_1())
#         print(module.task_2())
