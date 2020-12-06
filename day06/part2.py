def custom_customs(puzzle_input):
    sum_counts = 0

    for group in puzzle_input:
        lines = group.splitlines()
        chars = set(char for char in group if char != '\n')
        for char in chars:
            if len([line for line in lines if char in line]) == len(lines):
                sum_counts += 1

    return sum_counts


with open('puzzle_input.txt') as f:
    data = f.read()

puzzle_input = data.split('\n\n')
print(custom_customs(puzzle_input))
