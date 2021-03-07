input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    result = 0
    for value in array:
        if value <= 1 or result <= 1:
            result += value
        else:
            result *= value

    return result


result = find_max_plus_or_multiply(input)
print(result)