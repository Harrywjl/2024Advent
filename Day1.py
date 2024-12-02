import sys


def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("Day1Input.txt")

left_list = list()
right_list = list()
for i in file_data:
    line = i.split("   ")
    left_list.append(int(line[0]))
    right_list.append(int(line[1]))

# Part 1
"""
left = sys.maxsize
right = sys.maxsize
total = 0
for i in range(len(file_data)):
    total += abs(min(left_list)-min(right_list))
    left_list.remove(min(left_list))
    right_list.remove(min(right_list))
print(total)
"""

# Part 2

total = 0
for x in left_list:
    count = 0
    for y in right_list:
        if x == y:
            count += 1
    total += x * count
print(total)

