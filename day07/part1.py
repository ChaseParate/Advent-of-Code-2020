def part1(puzzle_input):
    bags = {}
    for bag in puzzle_input:
        bag_type, contained_bags = bag.split(' contain ')

        bag_type = bag_type[:-5]
        contained_bags = contained_bags[:-1].replace('bags', 'bag').split(' bag, ')
        contained_bags[-1] = contained_bags[-1][:-4]
        
        if 'no other' in contained_bags:
            bags[bag_type] = contained_bags
            continue

        #print(bag_type)
        #print(contained_bags)
        #print()

        bags[bag_type] = [b[2:] for b in contained_bags]

    # do funny list comprehension
    # revert to .values?
    good_bags = 0
    for bag, bag_contents in bags.items():
        if get_something_send_help(bags, bag_contents):
            good_bags += 1
    return good_bags
    
    

def part2(puzzle_input):
    pass


def get_something_send_help(bags, bag_contents):
    if 'shiny gold' in bag_contents:
        return True
    elif 'no other' in bag_contents:
        return False
    else:
        return any(get_something_send_help(bags, bags[inner_bag]) for inner_bag in bag_contents)
        #for inner_bag in bag_contents:
            #print(bag_contents)
            #print('help', inner_bag)
            #print(get_something_send_help(bags, bags[inner_bag]))
        

with open('input.txt') as f:
    data = f.read()

puzzle_input = data.splitlines()
print('Part 1:', part1(puzzle_input))
#print('Part 2:', part2(puzzle_input))
