def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


# for visualization
def print_map():
    for i in maze:
        print(i)


def move():
    direction = maze[row][col]
    r = row
    c = col
    i = 1
    if direction == "^":
        while maze[r - i][c] == ".":
            maze[r][c] = "X"
            maze[r - i][c] = "^"
            i+=1
    elif direction == "v":
        print()
    elif direction == "<":
        print()
    elif direction == ">":
        print()

    maze[row][col] = "X"


file_data = get_file_data("Day6Input.txt")
maze = []
for line in file_data:
    r = []
    r.append("*")
    for letter in line:
        r.append(letter)
    r.append("*")
    maze.append(r)
stars = []
for i in range(len(maze[0])):
    stars.append("*")
maze.insert(0, stars)
maze.append(stars)

row = 0
col = 0
# gets starting position
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == "^":
            row = i
            col = j

move()
print_map()
