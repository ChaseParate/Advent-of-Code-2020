def part1(puzzle_input):
    sum_counts = 0

    for line in puzzle_input:
        questions = set(char for char in line if char != '\n')
        sum_counts += len(questions)

    return sum_counts


def part2(puzzle_input):
    sum_counts = 0

    for group in puzzle_input:
        lines = group.splitlines()
        chars = set(char for char in group if char != '\n')
        for char in chars:
            if len([line for line in lines if char in line]) == len(lines):
                sum_counts += 1

    return sum_counts


with open('input.txt') as f:
    data = f.read()

puzzle_input = data.split('\n\n')
print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))
