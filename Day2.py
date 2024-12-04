def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

file_data = get_file_data("Day2Input.txt")

#Part 1

safe_count = 0
unsafe_count = 0
for i in file_data:
    report = i.split(" ")
    prev_level = int(report[0])
    prev_difference = 0
    safe = True
    for x in range (1,len(report)):
        current_level = int(report[x])
        current_difference = current_level - prev_level
        if x > 1:
            if (prev_difference <= 0 <= current_difference) or (prev_difference >= 0 >= current_difference):
                    safe = False
        if (abs(current_difference) == 0) or (abs(current_difference) > 3):
            safe = False
        prev_level = current_level
        prev_difference = current_difference
    if safe:
        safe_count += 1
    else:
        unsafe_count += 1

print(safe_count)
