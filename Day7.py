import math


def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

def binary_to_list(binary, total_operators):
    op_list = []
    for i in range(total_operators):
        x = total_operators - i
        print("binary: " + str(binary))
        print("2 to the power of " + str(x) + " = " + str(math.pow(2, x)))
        print(str(math.floor(binary / math.pow(2, x)) >= 1))
        if math.floor(binary / math.pow(2, x)) >= 1:
            op_list.insert(0, 1)
        else:
            op_list.insert(0, 0)
    print()
    return op_list


#test
print(str(binary_to_list(15, 5)))


file_data = get_file_data("Day7Input.txt")
sum = 0
for i in file_data:
    line = i.split(" ")

    target_num = line.pop(0)
    target_num = int(target_num[0:len(target_num) - 1])

    total_operators = len(line) - 1

    target_binary = int(math.pow(2, total_operators))

    """for binary in range(target_binary):
        # A list of 1's and 0's to sub as * or + respectively
        operator_list = binary_to_list(binary, total_operators)
        print(operator_list)"""


    """print(str(target_num))
    print(str(line))
    print(str(target_binary))
    print()"""
