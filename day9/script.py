import csv

data = []
FILE_PATH =  './day9/data.csv'
all_predicted_next_values = []
all_predicted_previous_values = []

with open(FILE_PATH) as file:
    reader = csv.reader(file, delimiter=' ')
    for line in reader:
        data.append([int(char) for char in line])


def expand_history(history):
    while (not all(value == 0 for value in history[-1])):
        last_array = history[-1]
        differences = []
        for index, _ in enumerate(last_array):
            if (index + 1 == len(last_array)): break
            differences.append(last_array[index + 1] - last_array[index])
        history.append(differences)
    history = [[0] + array + [0] for array in history]
    return history

def predict_values(history):
    expanded = expand_history([history])
    for index in range(len(expanded) - 2, -1, -1):
        expanded[index][-1] = expanded[index][-2] + expanded[index + 1][-1]
        expanded[index][0] = expanded[index][1] - expanded[index + 1][0]
    all_predicted_next_values.append(expanded[0][-1])
    all_predicted_previous_values.append(expanded[0][0])

for history in data:
    predict_values(history)

print('Next values sum: ', sum(all_predicted_next_values))
print('Previous values sum: ', sum(all_predicted_previous_values))

