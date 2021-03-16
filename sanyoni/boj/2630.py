import sys
from enum import Enum, auto


# enum
# https://www.daleseo.com/python-enum/
class StrEnum(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Color(StrEnum):
    Undefinded = auto()
    White = auto()
    Blue = auto()


def colored_paper(array):
    size = len(array[0])
    return colored_paper_inner(array, 0, 0, size)


def colored_paper_inner(array, x, y, size):
    if size == 1:
        if array[y][x] == 0:
            return [Color.White]
        else:
            return [Color.Blue]

    # 모든 색상이 같은 색상인지 판별합니다
    # 모든 색상이 같은 경우에는 다음 중 하나의 조건을 만족합니다
    # 1. 모든 색상이 0이여서 모든 색상의 합이 0입니다
    # 2. 모든 색상이 1이여서 (모든 색상의 합 / 면적)이 1 입니다
    sum_of_color = 0
    for row in range(y, y + size):
        for col in range(x, x + size):
            sum_of_color += array[row][col]

    color = Color.Undefinded

    if sum_of_color == 0:
        color = Color.White
    elif sum_of_color / (size * size) == 1:
        color = Color.Blue

    # 모든 색상이 같은 색상인 경우 그 색상을 반환합니다
    if color != Color.Undefinded:
        return [color]

    # 그렇지 않다면 다시 4개로 쪼개 검사합니다
    half_size = size // 2

    value = []
    value += colored_paper_inner(array, x, y, half_size)
    value += colored_paper_inner(array, x + half_size, y, half_size)
    value += colored_paper_inner(array, x, y + half_size, half_size)
    value += colored_paper_inner(array, x + half_size, y + half_size, half_size)

    return value


# 입력받은 값으로 색종이를 초기화합니다
size = int(sys.stdin.readline())
array = [[col for col in range(size)] for row in range(size)]
for row in range(size):
    input_row_splitted = sys.stdin.readline().rstrip().split()
    for col in range(size):
        array[row][col] = int(input_row_splitted[col])

# 색종이들을 자르고, 색종이들의 색상별 개수를 구합니다
color_array = colored_paper(array)
white_count = 0
blue_count = 0
for color in color_array:
    if color == Color.White:
        white_count += 1
    else:
        blue_count += 1

# 색종이들의 색상별 개수를 출력합니다
print(white_count)
print(blue_count)