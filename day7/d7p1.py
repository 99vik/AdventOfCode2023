import csv
import functools

HAND_TYPES = [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4], [5]]
HAND_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
file_path = './day7/camel_cards.csv'
data = []

with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    for line in csv_reader:
        data.append(line)

def get_type(cards):
    cards_splitted = [*cards]
    values = []
    while len(cards_splitted) > 0:
        x = cards_splitted.count(cards_splitted[0])
        values.append(x)
        cards_splitted = list(filter(lambda x: (x != cards_splitted[0]), cards_splitted))
    values.sort()
    return HAND_TYPES.index(values)

def first_item_greater(item1, item2):
    item1_splitted = [*item1]
    item2_splitted = [*item2]
    for i, _ in enumerate(item1_splitted):
        if (HAND_VALUES.index(item1_splitted[i]) == HAND_VALUES.index(item2_splitted[i])):
            continue
        elif (HAND_VALUES.index(item1_splitted[i]) > HAND_VALUES.index(item2_splitted[i])):
            return True
        else:
            return False

def hand_comparison(item1, item2):
    if (get_type(item1[0]) == get_type(item2[0])):
        if (first_item_greater(item1[0], item2[0])):
            return 1
        else:
            return -1
    elif (get_type(item1[0]) > get_type(item2[0])):
        return 1
    else:
        return -1
    

sorted_data = sorted(data, key=functools.cmp_to_key(hand_comparison))
result = sum(int(inner_array[1]) * (index + 1) for index, inner_array in enumerate(sorted_data))

print(result)

