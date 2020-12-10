import itertools
import re
from math import prod


def part1(puzzle_input):
    sorted_adapters = sorted(puzzle_input + [0, max(puzzle_input) + 3])
    difference = [sorted_adapters[i] - sorted_adapters[i-1] for i in
                  range(1, len(sorted_adapters))]
    return difference.count(1) * difference.count(3)


def part2(puzzle_input):
    num_dict = {2: 2, 3: 4, 4: 7}

    sorted_adapters = sorted(puzzle_input + [0, max(puzzle_input) + 3])
    difference = [str(sorted_adapters[i] - sorted_adapters[i-1]) for i in
                  range(1, len(sorted_adapters))]
    test = ''.join(difference)
    funny = re.findall('1{2,}3', test)

    return prod([num_dict[len(x) - 1] for x in funny])


with open('input.txt') as f:
    data = f.read()

puzzle_input = list(map(int, data.splitlines()))
print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))
