import math


def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


def get_indexes(search_num, search_list):
    indexes_list = []
    i = 0
    while i < len(search_list):
        if search_list[i] == search_num:
            indexes_list.append(i)
        i += 1
    return indexes_list


def comes_after(cur_page, cur_index, rule_indexes):
    cur_num = cur_page[cur_index]
    rules = []
    for y in rule_indexes:
        rules.append(x_rule[y])

    for index in range(cur_index + 1, len(cur_page)):
        elements_before = cur_page[index]
        for r in rules:
            if elements_before == r:
                return True
    return False


def comes_before(cur_page, cur_index, rule_indexes):
    cur_num = cur_page[cur_index]
    rules = []
    for x in rule_indexes:
        rules.append(y_rule[x])

    for index in range(0, cur_index):
        elements_after = cur_page[index]
        for r in rules:
            if elements_after == r:
                return True
    return False


file_data = get_file_data("Day5Input.txt")

pages = []
x_rule = []
y_rule = []
middle_pages = 0
for line in range(file_data.index("") + 1, len(file_data)):
    row = file_data[line].split(",")
    int_row = []
    for i in range(len(row)):
        int_row.append(int(row[i]))
    pages.append(int_row)

for i in range(0, file_data.index("")):
    rule = file_data[i]
    x_rule.append(int(rule[0:rule.index("|")]))
    y_rule.append(int(rule[rule.index("|") + 1:]))

valid_pages = []
for page in pages:
    valid = True
    i = 0
    # For each number on the page, find all the rules that relate to that number and check if valid
    while i < len(page):
        num = int(page[i])

        # check if everything that comes AFTER this number is valid
        #x_indexes contain the indexes of the rules in x_rule that is equal to num
        x_indexes = get_indexes(num, x_rule)
        if comes_after(page, i, x_indexes):
            valid = False
            print(str(page) + " is invalid (x) at index " + str(i))
            print()
            break
        # check if everything that comes BEFORE this number is valid
        # y_indexes contain the indexes of the rules in y_rule that is equal to num
        y_indexes = get_indexes(num, y_rule)
        if comes_before(page, i, y_indexes):
            valid = False
            print(str(page) + " is invalid (y) at index " + str(i))
            print()
            break

        i += 1

    if valid:
        valid_pages.append(page)

# Takes the middle values of all the valid pages and sums them up
for page in valid_pages:
    print(str(page))
    middle_pages += page[math.floor(len(page) / 2)]

print(middle_pages)
