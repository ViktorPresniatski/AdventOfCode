INPUT_FILE = 'input.txt'
OUTPUT_FILE = 'output.txt'


def read_file():
    with open(INPUT_FILE) as f:
        return f.read().split('\n')


def write_file(res):
    with open(OUTPUT_FILE, 'w') as f:
        f.write(str(res))


def run():
    file = read_file()
    n = int(file[0])

    res = 2 * n * (n + 1) // 2 + 2 * n + 1

    write_file(res)


run()



# sum 2 * (i + 1) = sum 2 * i + sum 2 = 2 * n * (n + 1) // 2 + 2 * n

