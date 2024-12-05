import re

def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

file_data = get_file_data("Day3Input.txt")
sum = 0

#Part 1
"""
for i in file_data:
    uncorrupted_list = re.findall("mul[(][0-9]+,[0-9]+[)]", i)
    for x in uncorrupted_list:
        sum += (int(x[x.index("(") + 1 : x.index(",")]) * int(x[x.index(",") + 1 : x.index(")")]))

print(sum)
"""

#Part 2

do = True
for i in file_data:
    uncorrupted_list = re.findall("mul[(][0-9]+,[0-9]+[)]|do[(][)]|don't[(][)]", i)
    for x in uncorrupted_list:
        if x == "do()":
            do = True
        if x == "don't()":
            do = False
        if do and "mul" in x:
            sum += (int(x[x.index("(") + 1 : x.index(",")]) * int(x[x.index(",") + 1 : x.index(")")]))

print(sum)