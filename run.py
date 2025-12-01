#!/Users/wpresniacki/.pyenv/shims/python
import importlib
import sys


def main():
    year = sys.argv[1]
    task = sys.argv[2]
    sub_task = sys.argv[3] if len(sys.argv) > 3 else None
    module = importlib.import_module(f'y{year}.t{task}')

    if sub_task:
        result = getattr(module, f'task_{sub_task}')()
        print(result)
    else:
        print(module.task_1())
        print(module.task_2())


if __name__ == '__main__':
    main()
