with open('Day3_input.txt') as f:
    data = [value.strip() for value in f.read().splitlines()]


def find_trees(data, right, down):
    return len([i for i in range(0, len(data), down) if data[i][int(i*right/down)%len(data[0])] == '#'])

    
print('Part 1: {}'.format(find_trees(data, 3, 1)))
print('part 2: {}'.format(find_trees(data,1,1)*find_trees(data,3,1)*find_trees(data,5,1)*find_trees(data,7,1)*find_trees(data,1,2)))
