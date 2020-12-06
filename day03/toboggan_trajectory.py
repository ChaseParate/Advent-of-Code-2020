def part1(puzzle_input):
    trees = 0
    for i, line in enumerate(puzzle_input):
        if line[(i * 3) % len(line)] == '#':
            trees += 1
    return trees


def part2(puzzle_input):
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

    product = 1
    for slope in slopes:
        trees = 0
        for i, line in enumerate(puzzle_input[::slope[1]]):
            if line[(i * slope[0]) % len(line)] == '#':
                trees += 1
        product *= trees

    return product


with open('input.txt') as f:
    data = f.read()

puzzle_input = data.splitlines()
print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))
