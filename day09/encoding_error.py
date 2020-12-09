import itertools


def part1(puzzle_input):
    preamble = 25
    for i, number in enumerate(puzzle_input[preamble:]):
        last_numbers_summed = set(map(sum, list(itertools.permutations(puzzle_input[i:i+preamble], r=2))))
        if number not in last_numbers_summed:
            return number


def part2(puzzle_input):
    invalid_number = part1(puzzle_input)

    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input[i+1:])):
            num_range = puzzle_input[i:i+j+1]
            if sum(num_range) == invalid_number:
                return min(num_range) + max(num_range)


with open('input.txt') as f:
    data = f.read()

puzzle_input = list(map(int, data.splitlines()))
print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))
