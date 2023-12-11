data = []
cols_with_galaxy = []
rows_without_galaxy = []
cols_without_galaxy = None
sum = 0
file = open('./day11/data.txt')
MULTIPLICATION_VALUE = 1000000

for index, line in enumerate(file):
    if (not cols_without_galaxy): cols_without_galaxy = list(range(len(line.rstrip())))
    if ('#' not in line):
        rows_without_galaxy.append(index)
        continue
    for index, char in enumerate(line):
        if (char == '#'): cols_with_galaxy.append(index)

cols_with_galaxy.sort()
rows_without_galaxy.sort()
cols_with_galaxy = list(set(cols_with_galaxy))
for i in cols_with_galaxy:
    cols_without_galaxy.remove(i)

file.seek(0)
for line_index, line in enumerate(file):
    galaxy_cols = []
    for index, char in enumerate(line):
        if (char == '#'): galaxy_cols.append(index)
    for index, col in enumerate(galaxy_cols):
        for x in cols_without_galaxy:
            if (x < col): galaxy_cols[index] += MULTIPLICATION_VALUE - 1
    data.append(galaxy_cols)

for starting_row, starting_galaxies in enumerate(data):
    for starting_col in starting_galaxies:
        for end_row, ending_galaxies in enumerate(data):
            for end_col in ending_galaxies:
                if starting_row > end_row or (starting_row == end_row and starting_col >= end_col): continue
                empty_rows_between = [num for num in rows_without_galaxy if starting_row < num < end_row]
                sum += abs(end_row - starting_row) + len(empty_rows_between)*(MULTIPLICATION_VALUE - 1) + abs(end_col - starting_col)

print(sum)

