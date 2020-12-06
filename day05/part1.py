def binary_boarding(puzzle_input):
    return max(partition_to_binary(partition) for partition in puzzle_input)


def partition_to_binary(partition):
    return int(partition.replace('F', '0').replace('L', '0')
               .replace('B', '1').replace('R', '1'), 2)


with open('puzzle_input.txt') as f:
    data = f.read()

puzzle_input = data.splitlines()
print(binary_boarding(puzzle_input))
