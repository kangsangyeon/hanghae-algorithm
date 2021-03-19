import sys
import collections


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


input_rows_count = int(sys.stdin.readline().rstrip())
input_rows_str = [sys.stdin.readline().rstrip() for i in range(input_rows_count)]
input_rows_array = [list(row) for row in input_rows_str]


def get_house_count(input_rows, x, y):
    direction_x = [0, 1, -1, 0, 0]
    direction_y = [0, 0, 0, 1, -1]
    directions_count = len(direction_x)

    house_count = 0
    next_visit = collections.deque()
    next_visit.append(Position(x, y))

    while len(next_visit) > 0:
        position = next_visit.pop()

        x = position.x
        y = position.y

        if input_rows[y][x] == "0":
            continue

        input_rows[y][x] = "0"
        house_count += 1

        for i in range(0, directions_count):
            next_x = x + direction_x[i]
            next_y = y + direction_y[i]

            if next_x < 0 or len(input_rows) <= next_x:
                continue

            if next_y < 0 or len(input_rows) <= next_y:
                continue

            if input_rows[next_y][next_x] == "1":
                next_visit.append(Position(next_x, next_y))

    return house_count


danji_list = list()

for row in range(input_rows_count):
    for col in range(input_rows_count):
        if input_rows_array[row][col] == "1":
            new_danji = get_house_count(input_rows_array, col, row)
            danji_list.append(new_danji)


danji_list.sort()

print(len(danji_list))
for danji in danji_list:
    print(danji)