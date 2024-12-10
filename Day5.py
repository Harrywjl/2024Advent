import math


def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("Day5Input.txt")

pages = []
x_rule = []
y_rule = []
middle_pages = 0
for line in range(file_data.index("") + 1, len(file_data)):
    row = file_data[line].split(",")
    pages.append(row)

for i in range(0, file_data.index("")):
    rule = file_data[i]
    x_rule.append(rule[0:rule.index("|")])
    y_rule.append(rule[rule.index("|") + 1])

valid_pages = []
for page in pages:
    valid = True
    i = 0
    while i < len(page):
        num = int(page[i])
        rules = filter(lambda x:x == num,x_rule)
        print(str(rules))

    if valid:
        valid_pages.append(page)

for page in valid_pages:
    middle_pages += page[math.floor(len(page) / 2)]

print(middle_pages)
