import regex as re

NUMBERS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
sum1 = 0
sum2 = 0

def find_first_num(array):
    for char in array:
        if char.isdigit(): return char

def find_matches(string):
    matches = re.findall("\d|one|two|three|four|five|six|seven|eight|nine", string, overlapped=True)
    first = matches[0] if matches[0].isdigit() else str(NUMBERS.index(matches[0]) + 1)
    last = matches[-1] if matches[-1].isdigit() else str(NUMBERS.index(matches[-1]) + 1)
    return int(first + last)

with open('./day1/data.txt') as file:
    for line in file:
        array = list(line)
        sum1 += (int(find_first_num(array) + find_first_num(reversed(array)))) 
        sum2 += find_matches(line)


print(sum1)
print(sum2)