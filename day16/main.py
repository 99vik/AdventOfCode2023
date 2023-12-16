import sys
sys.setrecursionlimit(5000)

layout = []
energized_tiles = []
memorized = tuple()

with open('./day16/data.txt') as file:
    for line in file:
        layout.append(line.strip())

def next(current_node, direction):
    if (direction == 'right'):
        return [current_node[0], current_node[1] + 1]
    elif (direction == 'left'):
        return [current_node[0], current_node[1] - 1]
    elif (direction == 'up'):
        return [current_node[0] - 1, current_node[1]]
    else:
        return [current_node[0] + 1, current_node[1]]

def beam(current_node, direction):
    global memorized
    row = current_node[0]
    col = current_node[1]
    if (row not in range(len(layout)) or col not in range(len(layout[0]))): return
    if ((current_node, direction) in memorized): return
    if (current_node not in energized_tiles): energized_tiles.append(current_node)
    memorized = memorized + ((current_node, direction),)
    o = layout[row][col]
    if (o == '.' or (direction in ['right', 'left'] and o == '-') or (direction in ['up', 'down'] and o == '|')):
        beam(next(current_node, direction), direction)
    if ((direction == 'right' and o == '/') or (direction == 'left' and o == '\\')):
        beam(next(current_node, 'up'), 'up')
    if ((direction == 'right' and o == '\\') or (direction == 'left' and o == '/')):
        beam(next(current_node, 'down'), 'down')
    if ((direction == 'up' and o == '/') or (direction == 'down' and o == '\\')):
        beam(next(current_node, 'right'), 'right')
    if ((direction == 'up' and o == '\\') or (direction == 'down' and o == '/')):
        beam(next(current_node, 'left'), 'left')
    if (direction in ['right', 'left'] and o == '|'):
        beam(next(current_node, 'down'), 'down')
        beam(next(current_node, 'up'), 'up')
    if (direction in ['up', 'down'] and o == '-'):
        beam(next(current_node, 'left'), 'left')
        beam(next(current_node, 'right'), 'right')
    
beam([0, 0], 'right')
print(f'Part 1: {len(energized_tiles)}')

starting_nodes = []

for i, _ in enumerate(layout[0]):
    starting_nodes.append([[0, i], 'down'])
for i, _ in enumerate(layout[-1]):
    starting_nodes.append([[len(layout) - 1, i], 'up'])
for i, _ in enumerate(layout):
    starting_nodes.append([[i, 0], 'right'])
for i, _ in enumerate(layout):
    starting_nodes.append([[i, len(layout[0]) - 1], 'left'])

sums = []
for i, node in enumerate(starting_nodes):
    memorized = tuple()
    energized_tiles = []
    beam(node[0], node[1])
    sums.append(len(energized_tiles))
    print(f'{i + 1}/{len(starting_nodes)}')

print(f'Part 2: {max(sums)}')

