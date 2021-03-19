import sys


def compress_quad_tree(data_array: list[str], x: int, y: int, size: int):

    is_all_color_same = True
    first_color = data_array[y][x]
    for row in range(y, y + size):
        for col in range(x, x + size):
            # 하나라도 다른 색상이 발견된다면 "모든 색상이 같지 않다는 것"을 알 수 있기 위해
            # 플래그 값을 갱신합니다
            if data_array[row][col] != first_color:
                is_all_color_same = False
                break

        # 모두 같은 색상이 아닌게 밝혀졌다면 더 이상 색상 검사를 할 필요가 없습니다.
        if is_all_color_same == False:
            break

    # 모든 색상이 같다면 그 색상을 반환합니다
    if is_all_color_same == True:
        return f"{first_color}"

    half_size = size // 2
    upper_left = compress_quad_tree(data_array, x, y, half_size)
    upper_right = compress_quad_tree(data_array, x + half_size, y, half_size)
    lower_left = compress_quad_tree(data_array, x, y + half_size, half_size)
    lower_right = compress_quad_tree(data_array, x + half_size, y + half_size, half_size)

    return f"({upper_left}{upper_right}{lower_left}{lower_right})"


data_rows_count = int(sys.stdin.readline().rstrip())
data_rows = []
for i in range(data_rows_count):
    data_rows.append(sys.stdin.readline().rstrip())

print(compress_quad_tree(data_rows, 0, 0, data_rows_count))