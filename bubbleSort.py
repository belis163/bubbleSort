import sys
import json


def bubbleSort(tableToSort):
    result = tableToSort
    for index in range(len(result) - 1, 0, -1):
        for i in range(index):
            if result[i] > result[i + 1]:
                tmp = result[i]
                result[i] = result[i + 1]
                result[i + 1] = tmp
    return result

file = open(sys.argv[1])
data = json.load(file)

nieposortowana = data['input_list']

print("\nNieposortowana: \n")
print(nieposortowana)
posortowana = bubbleSort(nieposortowana)
print("\nPsortowana: \n")
print(posortowana)


