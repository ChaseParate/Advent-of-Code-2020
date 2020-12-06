def part1(puzzle_input):
    valid_passwords = 0
    for line in puzzle_input:
        policy, password = line.split(':')

        letter = policy[-1]
        min_range, max_range = map(int, policy[:-2].split('-'))

        if password.count(letter) in range(min_range, max_range + 1):
            valid_passwords += 1

    return valid_passwords


def part2(puzzle_input):
    valid_passwords = 0
    for line in puzzle_input:
        policy, password = line.split(':')

        letter = policy[-1]
        index1, index2 = map(int, policy[:-2].split('-'))
        pos1, pos2 = password[index1] == letter, password[index2] == letter

        if (pos1 and not pos2) or (not pos1 and pos2):
            valid_passwords += 1

    return valid_passwords


with open('input.txt') as f:
    data = f.read()

puzzle_input = data.splitlines()
print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))
