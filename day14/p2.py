CYCLES = 1000000000

input_data = tuple()
with open('./day14/data.txt') as file:
    for line in file:
        input_data = input_data + (tuple((line.strip())),)

def tilt_up(data):
    tilted_data = []
    for i in range(len(data[0])):
        column = []
        for j in range(len(data)):
            column.append(data[j][i])
        column = ''.join(column).split('#')
        for i, _ in enumerate(column):
            column[i] = ''.join(sorted(column[i], key=lambda x: x != 'O'))
        column = list('#'.join(column))
        column.reverse()
        tilted_data.append(tuple(column))
    tilted_data = tuple(tilted_data)
    return tilted_data

def cycle(data):
    for _ in range(4):
        data = tilt_up(data)
    return data

def cycle_n(data):
    seen_states = {}
    for i in range(CYCLES):
        data = cycle(data)
        state = [''.join(line) for line in data]
        if (data in seen_states):
            return list(seen_states)[list(seen_states).index((data)):][((CYCLES - list(seen_states).index((data))) % len(list(seen_states)[list(seen_states).index((data)):])) - 1]
        seen_states[data] = state
    return data

def calculate_load(data):
    ans = 0
    for i, col in enumerate(data):
        for x in col:
            if x == 'O':
                ans += len(data) - i
    return ans

cycled_data = cycle_n(input_data)

load = calculate_load(cycled_data)
print(load)
