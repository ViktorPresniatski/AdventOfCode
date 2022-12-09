import inspect
from pathlib import Path


def read_file(filename):
    return open(filename).read()


def read(t=str, group=False):
    prev_exec_func = inspect.stack()[1][0]
    cur_module = inspect.getmodule(prev_exec_func)
    cur_path = Path(cur_module.__file__)
    task_number = cur_path.stem.lstrip('t')
    input_file = Path(cur_module.__file__).parent / 'data' / f'input{task_number}.txt'
    text = read_file(input_file)
    if group:
        return list(map(lambda a: list(map(t, a.split('\n'))), text.split('\n\n')))
    return list(map(t, text.split('\n')))


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
