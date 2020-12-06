def binary_boarding(puzzle_input):
    boarding_passes = sorted(partition_to_binary(partition)
                             for partition in puzzle_input)

    for i in range(1, len(boarding_passes) - 1):
        a, b = boarding_passes[i], boarding_passes[i + 1]
        if b - a == 2:
            return a + 1


def partition_to_binary(partition):
    return int(partition.replace('F', '0').replace('L', '0')
               .replace('B', '1').replace('R', '1'), 2)


with open('puzzle_input.txt') as f:
    data = f.read()

puzzle_input = data.splitlines()
print(binary_boarding(puzzle_input))
