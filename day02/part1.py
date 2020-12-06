def password_philosophy(puzzle_input):
    valid_passwords = 0
    for line in puzzle_input:
        policy, password = line.split(':')

        letter = policy[-1]
        min_range, max_range = map(int, policy[:-2].split('-'))

        if password.count(letter) in range(min_range, max_range + 1):
            valid_passwords += 1

    return valid_passwords


with open('puzzle_input.txt') as f:
    data = f.read()

puzzle_input = data.splitlines()
print(password_philosophy(puzzle_input))
