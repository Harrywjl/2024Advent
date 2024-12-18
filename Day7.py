def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("Day7Input.txt")
sum = 0
for i in file_data:
    line = i.split(" ")
    target = int(line[0][0:len(line[0]) - 1])
    binary = 0
    #use a list of 1's and 0's to sub as + or *
    print(str(target))
    print(str(line))