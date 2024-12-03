def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

file_data = get_file_data("Day2Input.txt")

safe_count = 0
unsafe_count = 0
for i in file_data:
    report = i.split(" ")
    prev_level = int(report[0])
    prev_difference = 0
    safe = True
    print("Report")
    print(" Level 0: " + str(prev_level))
    for x in range (1,len(report)):
        current_level = int(report[x])
        print(" Level " + str(x) + ": " + str(current_level))
        current_difference = current_level - prev_level
        print(" Dif: " + str(current_difference))
        if x > 1:
            #if opposite signs or the same
            if (prev_difference < 0 < current_difference) or (prev_difference > 0 > current_difference) or (prev_difference == current_difference):
                #if
                #levels differ by more than 3
                    safe = False
        prev_level = current_level
        prev_difference = current_difference
    if safe:
        safe_count += 1
    else:
        unsafe_count += 1

print(safe_count)
