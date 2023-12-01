INPUT_FILE = 'input.txt'
OUTPUT_FILE = 'output.txt'


def read_file():
	with open(INPUT_FILE) as f:
		return f.read().split('\n')


def write_file(res):
	with open('output.txt', 'w') as f:
		f.write(str(res))


def run():
	file = read_file()

	write_file(file)


run()