data = []
with open('./day14/data.txt') as file:
    for line in file:
        data.append(list(line.strip()))

def f():
    tilted_data = []
    ans = 0
    for i in range(len(data[0])):
        column = []
        for j in range(len(data)):
            column.append(data[j][i])
        column = ''.join(column).split('#')
        for i, _ in enumerate(column):
            column[i] = ''.join(sorted(column[i], key=lambda x: x != 'O'))
        tilted_data.append(list('#'.join(column)))
    for col in tilted_data:
        for i, x in enumerate(col):
            if x == 'O':
                ans += len(col) - i
    return ans

ans = f()
print(ans)
