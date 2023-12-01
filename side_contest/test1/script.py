INPUT_FILE = 'input.txt'
OUTPUT_FILE = 'output.txt'


def read_file():
	with open(INPUT_FILE) as f:
		return f.read().split('\n')


def write_file(res):
	with open('output.txt', 'w') as f:
		f.write(str(res))


def run():
	matr = read_file()[1:]
	res = sum([sum(map(int, row.split())) for row in matr])
	write_file(res)


run()