def report_repair(puzzle_input):
    for i, num1 in enumerate(puzzle_input):
        for j, num2 in enumerate(puzzle_input[i+1:]):
            if num1 + num2 == 2020:
                return num1 * num2


with open('puzzle_input.txt') as f:
    data = f.read()

puzzle_input = list(map(int, data.splitlines()))
print(report_repair(puzzle_input))
