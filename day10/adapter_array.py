import re
from math import prod


def part1(puzzle_input):
    sorted_adapters = sorted(puzzle_input + [0, max(puzzle_input) + 3])
    difference = [sorted_adapters[i] - sorted_adapters[i-1] for i in
                  range(1, len(sorted_adapters))]
    # [1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 3, ...]
    
    return difference.count(1) * difference.count(3)


def part2(puzzle_input):
    sorted_adapters = sorted(puzzle_input + [0, max(puzzle_input) + 3])
    difference = [sorted_adapters[i] - sorted_adapters[i-1] for i in
                  range(1, len(sorted_adapters))]
    # [1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 3, ...]

    difference_string = ''.join(map(str, difference))
    # '11113111131113...'

    lengths = map(len, re.findall('(1{2,})3', difference_string))
    # [4, 4, 3, ...]

    return prod(map(tribonacci_sequence, lengths))


def tribonacci_sequence(n):
    a, b, c = 0, 0, 1
    for i in range(n):
        a, b, c = b, c, a + b + c
    return c


with open('input.txt') as f:
    data = f.read()

puzzle_input = list(map(int, data.splitlines()))
print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))
