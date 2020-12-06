def password_philosophy(puzzle_input):
    valid_passwords = 0
    for line in puzzle_input:
        policy, password = line.split(':')

        letter = policy[-1]
        index1, index2 = map(int, policy[:-2].split('-'))
        pos1, pos2 = password[index1] == letter, password[index2] == letter

        if (pos1 and not pos2) or (not pos1 and pos2):
            valid_passwords += 1

    return valid_passwords


with open('puzzle_input.txt') as f:
    data = f.read()

puzzle_input = data.splitlines()
print(password_philosophy(puzzle_input))
