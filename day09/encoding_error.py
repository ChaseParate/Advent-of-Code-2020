import itertools


def part1(puzzle_input):
    preamble = 25
    for i, number in enumerate(puzzle_input[preamble:]):
        last_numbers_summed = set(map(sum, list(itertools.permutations(
            puzzle_input[i:i + preamble], r=2))))
        if number not in last_numbers_summed:
            return number


def part2(puzzle_input):
    invalid_number = part1(puzzle_input)
    invalid_index = puzzle_input.index(invalid_number)

    for start in range(invalid_index):
        prefix_sum = list(itertools.accumulate(
            puzzle_input[start:invalid_index - 1]))

        if invalid_number in prefix_sum:
            end_range = start + prefix_sum.index(invalid_number) + 1
            contiguous_range = puzzle_input[start:end_range]
            return min(contiguous_range) + max(contiguous_range)


with open('input.txt') as f:
    data = f.read()

puzzle_input = list(map(int, data.splitlines()))
print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))
