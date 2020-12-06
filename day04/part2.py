from string import hexdigits


def passport_processing(puzzle_input):
    valid_passports = 0
    for passport in puzzle_input:
        if verify_passport(passport):
            valid_passports += 1

    return valid_passports


def verify_passport(passport):
    fields = [k for k in passport.replace('\n', ' ').split(' ')]
    keys = {f.split(':')[0]: f.split(':')[1] for f in fields}

    for field in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'):
        if field not in keys:
            return

    verification = [
        int(keys['byr']) in range(1920, 2003),
        int(keys['iyr']) in range(2010, 2021),
        int(keys['eyr']) in range(2020, 2031),

        len(keys['hgt']) >= 3 and int(keys['hgt'][:-2]) in
        range(150, 194) if keys['hgt'][-2:] == 'cm' else range(59, 76),

        keys['hcl'] and keys['hcl'][0] == '#' and len(keys['hcl']) == 7 and
        all(_ in hexdigits for _ in keys['hcl'][1:]),

        keys['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        keys['pid'].isdigit() and len(keys['pid']) == 9
    ]

    return all(verification)


with open('puzzle_input.txt') as f:
    data = f.read()

puzzle_input = data.split('\n\n')
print(passport_processing(puzzle_input))
