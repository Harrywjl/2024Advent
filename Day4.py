def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("Day4Input.txt")

# build a 2D List based on the file_data
grid = []
for line in file_data:
    row = []
    for letter in line:
        row.append(letter)
    grid.append(row)


#Part 1
"""
count = 0
key = "XMAS"
row_len = len(grid[0])
col_len = len(grid)
key_len = len(key)

# horizontal

for row in range(col_len):
    for column in range(row_len - key_len + 1):
        letter_for = ""
        for i in range(key_len):
            letter_for += grid[row][column + i]
        if letter_for == key:
            count += 1
        letter_bac = ""
        for i in range(key_len):
            letter_bac += grid[row][row_len - 1 - column - i]
        if letter_bac == key:
            count += 1

# vertical 

for column in range(row_len):
    for row in range(col_len - key_len + 1):
        letter_for = ""
        for i in range(key_len):
            letter_for += grid[row + i][column]
        if letter_for == key:
            count += 1
        letter_bac = ""
        for i in range(key_len):
            letter_bac += grid[col_len - 1 - row - i][column]
        if letter_bac == key:
            count += 1

# diagonal

for row in range(col_len - key_len + 1):
    for column in range(row_len - key_len + 1):

        letter_for_up = ""
        for i in range(key_len):
            letter_for_up += grid[col_len - 1 - row - i][column + i]
        if letter_for_up == key:
            count += 1

        letter_for_down = ""
        for i in range(key_len):
            letter_for_down += grid[row + i][column + i]
        if letter_for_down == key:
            count += 1

        letter_bac_up = ""
        for i in range(key_len):
            letter_bac_up += grid[col_len - 1 - row - i][row_len - 1 - column - i]
        if letter_bac_up == key:
            count += 1

        letter_bac_down = ""
        for i in range(key_len):
            letter_bac_down += grid[row + i][row_len - 1 - column - i]
        if letter_bac_down == key:
            count += 1
"""
#Part 2

count = 0
key = "MAS"
row_len = len(grid[0])
col_len = len(grid)
key_len = len(key)


for row in range(1, col_len - 1):
    for column in range(1, row_len - 1):
        mas_count = 0

        letter_for_up = ""
        for i in range(key_len):
            letter_for_up += grid[row - i + 1][column + i - 1]
        if letter_for_up == key:
            mas_count += 1

        letter_for_down = ""
        for i in range(key_len):
            letter_for_down += grid[row + i - 1][column + i - 1]
        if letter_for_down == key:
            mas_count += 1

        letter_bac_up = ""
        for i in range(key_len):
            letter_bac_up += grid[row - i + 1][column - i + 1]
        if letter_bac_up == key:
            mas_count += 1

        letter_bac_down = ""
        for i in range(key_len):
            letter_bac_down += grid[row + i - 1][column - i + 1]
        if letter_bac_down == key:
            mas_count += 1

        if mas_count == 2:
            count += 1

print(count)
