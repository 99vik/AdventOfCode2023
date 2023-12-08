STEPS = 'LLLRRLRRRLLRRLRRLLRLRRLRRRLRRLRRLRRRLRLRRLRLRRLRRLLRRLRLLRRLLLRRRLRRLRLRLRRRLRLLRRLRRRLRRLRRLRRLRLLRLLRRLRRRLRRLRLRRLRRRLRRLLRLLRRLRRRLLRRRLRLRRRLLRLRRLRRLLRRLRRLLLRRRLRLRRRLRRLLRLRRLRLLRRRLRLRLLRLRRRLRLRRRLRRLRLRLLRLRRRLRRLRRRLRRRLRLRRRLRRRLLLLRLRLRRRLLLRLRRRLRRLRLRRLLRLLRRRR'
STARTING_NODE = 'AAA'
FINISH_NODE = 'ZZZ'

data = {}

def clean_line(line):
    cleaned_line = line.split(' = ')
    cleaned_line[1] = cleaned_line[1].strip('\n()',).split(', ')
    return cleaned_line

with open('./day8/data.txt') as file:
    for line in file:
        cleaned = clean_line(line)
        data[cleaned[0]] = {'L': cleaned[1][0], 'R': cleaned[1][1]}

current_node = STARTING_NODE
counter = 0
instruction_counter = 0

while (current_node != FINISH_NODE):
    current_node = data[current_node][STEPS[instruction_counter]]
    counter += 1
    instruction_counter = (0 if instruction_counter == (len(STEPS) - 1) else instruction_counter + 1)

print(counter)





