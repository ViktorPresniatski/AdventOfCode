#!/Users/presniatski/miniconda3/bin/python
import importlib
import sys


def main():
    task = sys.argv[1]
    module = importlib.import_module(f'contest.{task}.script')
    module.run()


if __name__ == '__main__':
    main()
