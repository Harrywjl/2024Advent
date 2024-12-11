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
        i+=1
    return indexes_list

def breaks_x_rule(page, cur_index, rule_indexes):

def breaks_y_rule(page, cur_index, rule_indexes):

    


file_data = get_file_data("Day5Input.txt")

pages = []
x_rule = []
y_rule = []
middle_pages = 0
for line in range(file_data.index("") + 1, len(file_data)):
    row = file_data[line].split(",")
    for i in range(len(row)):
        row[i] = int(row[i])
    pages.append(row)

for i in range(0, file_data.index("")):
    rule = file_data[i]
    x_rule.append(int(rule[0:rule.index("|")]))
    y_rule.append(int(rule[rule.index("|") + 1:]))

valid_pages = []
for page in pages:
    valid = True
    i = 0
    #For each number on the page, find all the rules that relate to that number and check if valid
    while i < len(page):
        num = int(page[i])
        
        #check if everything that comes BEFORE this number is valid
        x_indexes = get_indexes(num, x_rule)
        

        #check if everything that comes AFTER this number is valid
        y_indexes = get_indexes(num, y_rule)
        
        i+=1

    if valid:
        valid_pages.append(page)

#Takes the middle values of all the valid pages and sums them up
for page in valid_pages:
    middle_pages += page[math.floor(len(page) / 2)]

print(middle_pages)
