import math

# 절단기의 높이를 매개변수로 건네준 높이로 설정하고 잘랐을 때 충분한 양의 나무를 수확할 수 있는지에 대한 여부를 확인합니다
# return[0]: 필요한 "최소 나무의 양" 이상을 얻을 수 있는지, 즉 충분히 수확할 수 있는지에 대한 여부입니다
# return[1]: "절단해서 얻는 나무의 양"이 "최소 나무의 양"과 일치하는, 즉 가장 이상적인 높이라면 True입니다
def is_over_gaining_after_cutting(_tree_list: [], _cutting_height, _least_amount: int):

    sum_amount_after_cutting = 0
    for _tree in _tree_list:
        # 절단기의 높이보다 낮은 나무는 절단기에 잘리지 않습니다
        if _cutting_height >= _tree:
            continue

        # 절단기로 자르고 난 뒤 얻을 수 있는 나무의 양을 누적합니다
        sum_amount_after_cutting += _tree - _cutting_height

        # 누적된 양이 최소 양보다 많다면 반복을 멈추고 양이 많다는 것을 반환합니다
        if sum_amount_after_cutting > _least_amount:
            return True, False

    if sum_amount_after_cutting == _least_amount:
        return True, True
    else:
        return False, False


# 가장 이상적인 절단기의 높이를 찾아 반환합니다
def search_ideal_height(tree_list: [], _least_amount: int):
    tree_list_length = len(tree_list)
    start = 0
    end = tree_list[tree_list_length - 1]
    ideal_height = 0

    while start <= end:
        height = (start + end) // 2

        # 절단기의 높이를 현재 높이로 정하고 잘랐을 때 충분한 나무를 얻을 수 있는지 판별합니다
        gaining_info = is_over_gaining_after_cutting(tree_list, height, _least_amount)

        # "잘린 나무의 양"이 "원하는 나무의 양"과 정확히 일치한다면
        # 지금 설정한 절단기의 높이가 최적의 높이입니다.
        if gaining_info[1] == True:
            return height

        # "잘린 나무의 양"이 "원하는 나무의 양"보다 많으면 탐색 범위를 위로 좁히고,
        # 반대로 적다면 탐색 범위를 아래로 좁혀 다시 탐색합니다
        if gaining_info[0]:
            start = height + 1

            ideal_height = height
        else:
            end = height - 1

    return ideal_height


tree_count, least_length = input().split()
tree_count = int(tree_count)
least_length = int(least_length)

input_tree_list_splitted = input().split()

tree_list = []
for i in range(0, tree_count):
    tree_list.append(int(input_tree_list_splitted[i]))

# "절단기로 자른 후 얻을 수 있는 나무들의 양"을 쉽게 얻을 수 있기 하기 위해
# 나무들을 오름차순으로 정렬합니다
tree_list.sort()

value = search_ideal_height(tree_list, least_length)
print(value)
