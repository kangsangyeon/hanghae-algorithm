input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    max_num = input[0]
    for current_number in array:
        if max_num < current_number:
            max_num = current_number

    return max_num


result = find_max_num(input)
print(result)