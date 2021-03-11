# 정렬된 array와 값을 입력받고, 전달받은 값의 array 내 lower bound 위치를 구합니다
def get_lower_bound_position(sorted_array, value):
    # 만약 입력받은 값이 정렬된 배열의 맨 마지막 요소보다 크다면
    # 적정 위치는 이 배열의 크기를 벗어나므로 탐색을 하지 않고 맨 마지막 인덱스를 건네줍니다
    if sorted_array[len(sorted_array) - 1] < value:
        return len(sorted_array)

    # 입력받은 값이 배열 내에 존재하게 된다면 lower_bound 위치를 찾아냅니다
    start = 0
    end = len(sorted_array) - 1

    lower_bound_position = 0

    while start <= end:
        cursor = (start + end) // 2

        if sorted_array[cursor] < value:
            start = cursor + 1
        else:
            end = cursor - 1
            lower_bound_position = cursor

    return lower_bound_position


# 전달한 array의 LIS의 길이를 반환하는 함수입니다
# 주의) lower_bound_list의 요소들이 곧 LIS의 요소들임을 말하는 것은 아닙니다.
# 단지 요소들을 순회하면서 지금까지 나왔던 모든 부분집합 중 가장 긴 부분집합의 길이만을 구하기 위한 용도입니다
def get_lis_length(array):
    lower_bound_list = []
    lower_bound_list.append(array[0])

    for i in range(1, len(array)):
        item = array[i]

        lower_bound_position = get_lower_bound_position(lower_bound_list, item)
        if lower_bound_position == len(lower_bound_list):
            lower_bound_list.append(item)
        else:
            lower_bound_list[lower_bound_position] = item

    return len(lower_bound_list)


input_array_length = int(input())
input_array = input().split()
input_array_to_int = []
for item in input_array:
    input_array_to_int.append(int(item))

print(get_lis_length(input_array_to_int))