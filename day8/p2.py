import math

STEPS = 'LLLRRLRRRLLRRLRRLLRLRRLRRRLRRLRRLRRRLRLRRLRLRRLRRLLRRLRLLRRLLLRRRLRRLRLRLRRRLRLLRRLRRRLRRLRRLRRLRLLRLLRRLRRRLRRLRLRRLRRRLRRLLRLLRRLRRRLLRRRLRLRRRLLRLRRLRRLLRRLRRLLLRRRLRLRRRLRRLLRLRRLRLLRRRLRLRLLRLRRRLRLRRRLRRLRLRLLRLRRRLRRLRRRLRRRLRLRRRLRRRLLLLRLRLRRRLLLRLRRRLRRLRLRRLLRLLRRRR'

data = {}

def clean_line(line):
    cleaned_line = line.split(' = ')
    cleaned_line[1] = cleaned_line[1].strip('\n()',).split(', ')
    return cleaned_line

with open('./day8/data.txt') as file:
    for line in file:
        cleaned = clean_line(line)
        data[cleaned[0]] = {'L': cleaned[1][0], 'R': cleaned[1][1]}

def get_all_starting_nodes():
    starting_nodes = []
    for key in data.keys():
        if (key.endswith('A')): starting_nodes.append(key) 
    return starting_nodes

starting_nodes = get_all_starting_nodes()
each_node_counter = []

for starting_node in starting_nodes:
    counter = 0
    instruction_counter = 0
    current_node = starting_node
    while (not current_node.endswith('Z')):
        current_node = data[current_node][STEPS[instruction_counter]]
        instruction_counter = (0 if instruction_counter == (len(STEPS) - 1) else instruction_counter + 1)
        counter += 1
    each_node_counter.append(counter)

print(math.lcm(*each_node_counter))


