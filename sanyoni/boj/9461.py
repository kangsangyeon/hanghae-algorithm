# 나선에 있는 N번째 삼각형의 변 길이를 구합니다
triangles_length_list = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]


def get_triangles_length(index):
    global triangles_length_list

    for i in range(len(triangles_length_list), index + 1):
        value1 = triangles_length_list[i - 1]
        value2 = triangles_length_list[i - 5]

        triangles_length_list.append(value1 + value2)

    return triangles_length_list[index]


testcase_count = int(input())
for i in range(0, testcase_count):
    input_number = int(input())
    print(get_triangles_length(input_number))