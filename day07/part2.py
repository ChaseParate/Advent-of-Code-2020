def part2(puzzle_input):
    bags = {}
    for bag in puzzle_input:
        bag_type, contained_bags = bag.split(' contain ')

        bag_type = bag_type[:-5]
        contained_bags = contained_bags[:-1].replace('bags', 'bag').split(' bag, ')
        contained_bags[-1] = contained_bags[-1][:-4]
        
        if 'no other' in contained_bags:
            bags[bag_type] = contained_bags
            continue

        bags[bag_type] = []
        for contained_bag in contained_bags:
            count = int(contained_bag[:2])
            for i in range(count):
                bags[bag_type].append(contained_bag[2:])

    #print(bags['shiny gold'])
    return get_something_send_help(bags, bags['shiny gold'])


# edit function so that instead of returning T/F, returning number that eventually gets summed?
# maybe just pass in bag instead of bag_contents for debugging?
def get_something_send_help(bags, bag_contents):
    if 'no other' in bag_contents:
        return 0
    else:
        #print(bag_contents)
        #print(len(bag_contents))
        test = len(bag_contents)
        #print()
        for inner_bag in bag_contents:
            #print(inner_bag, test)
            test += get_something_send_help(bags, bags[inner_bag])
        return test

        #return len(bag_contents) + sum(get_something_send_help(bags, bags[inner_bag]) for inner_bag in bag_contents)
        


with open('input.txt') as f:
    data = f.read()

puzzle_input = data.splitlines()
print('Part 2:', part2(puzzle_input))
