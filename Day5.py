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
for line in range(file_data.index("") + 1, len(file_data)):
    row = file_data[line].split(",")
    pages.append(row)

for i in range(0, file_data.index("")):
    rule = file_data[i]
    x_rule.append(rule[0, rule.index(",")])
    y_rule.append(rule[rule.index(",") + 1])

