import sys


def get_number_of_kinds(tiles_count):

    if tiles_count <= 2:
        return tiles_count

    prev_prev_value = 1
    prev_value = 2
    value = 0

    for i in range(3, tiles_count + 1):
        value = (prev_prev_value + prev_value) % 15746

        prev_prev_value = prev_value
        prev_value = value

    return value


n = int(sys.stdin.readline().rstrip())
print(get_number_of_kinds(n))