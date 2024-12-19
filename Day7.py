import math
from functools import cache


def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


def binary_to_list(binary, total_operators):
    op_list = []
    total = binary
    for i in range(total_operators):
        x = total_operators - i - 1
        if math.floor(total / math.pow(2, x)) >= 1:
            op_list.insert(0, 1)
            total %= math.pow(2, x)
        else:
            op_list.insert(0, 0)
    return op_list


"""@cache
def takeAndSkip(targetSum, nums, currentNum):
    if currentNum == targetSum:
        return True

    if currentNum > targetSum: return False

    for i in range(0, len(nums), 1):
        if takeAndSkip(targetSum, nums, currentNum * nums[i]) or takeAndSkip(targetSum, nums, currentNum + nums[i]): return True

    return False"""


file_data = get_file_data("Day7Input.txt")
final_sum = 0
for i in file_data:
    line = i.split(" ")

    target_num = line.pop(0)
    target_num = int(target_num[0:len(target_num) - 1])

    total_operators = len(line) - 1

    target_binary = int(math.pow(2, total_operators))

    for binary in range(target_binary):
        num = int(line[0])
        # A list of 1's and 0's to sub as * or + respectively
        """operator_list = binary_to_list(binary, total_operators)
        for x in range(len(operator_list)):
            operations = operator_list[x]
            if operations == 0:
                final_sum += int(line[x + 1])
            else:
                final_sum *= int(line[x + 1])"""
        print(str(target_num))
        print(str(num))
        print()
        if takeAndSkip(target_num, line, 0):
            final_sum += target_num
        """if num == target_num:
            final_sum += target_num"""


print(str(final_sum))
