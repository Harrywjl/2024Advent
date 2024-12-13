def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


# for visualization
def print_map(map_arr):
    for row in map_arr:
        print(row)


file_data = get_file_data("Day6Input.txt")
row = 0
col = 0
# gets starting position
for i in range(len(file_data)):
    for j in range(len(file_data[i])):
        if file_data[i][j]:
            row = i
            col = j