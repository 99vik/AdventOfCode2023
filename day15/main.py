import csv
import re

data = None
with open('./day15/data.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for input in csv_reader:
        data = input

def f(string):
    value = 0
    for char in string:
        av = ord(char)
        value += av
        value *= 17
        value %= 256
    return value

boxes = {}
for i in range(256):
    boxes[i] = {}

for string in data:
    label = "".join(re.findall("[a-zA-Z]+", string))
    box_n = f(label)
    if ('-' in string):
        if (boxes[box_n].get(label)):
            del boxes[box_n][label]
    else:
        boxes[box_n][label] = int(string[-1])

ans1, ans2 = 0, 0
for string in data:
    ans1 += f(string)
for n, lenses in boxes.items():
    for x, i in enumerate(list(lenses.items())):
        ans2 += (n + 1) * (x + 1) * i[1]
print(f'Part 1: {ans1}')
print(f'Part 2: {ans2}')
