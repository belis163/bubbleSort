import sys
import json


def bubbleSort(tableToSort):
    result = tableToSort
    for i in range(0, len(result) - 1):
        for j in range(0, len(result)-i-1):
            if result[j] > result[j + 1]:
                result[j], result[j+1] = result[j+1], result[j]
                
    return result

file = open(sys.argv[1])
data = json.load(file)

nieposortowana = data['input_list']

print("\nNieposortowana: \n")
print(nieposortowana)
posortowana = bubbleSort(nieposortowana)
print("\nPsortowana: \n")
print(posortowana)


