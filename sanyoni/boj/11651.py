import random


def quick_sort(array, comparer):
    quick_sort_inner(array, 0, len(array), comparer)


def quick_sort_inner(array, start, end, comparer):
    # 재귀 종료조건입니다
    # 정렬할 요소가 2개 이상이 아니라면 정렬이 필요하지 않습니다
    if (end - start) <= 1:
        return

    # 범위 안의 맨 첫번째 요소를 "중심 비교요소"로 설정합니다
    # 아래 루틴을 통해 범위 안의 요소들은 "중심 비교요소"를 중심으로, 왼쪽에는 이보다 작은 요소들이,
    # 오른쪽에는 이보다 큰 요소들이 위치하게 됩니다
    pivot = start

    # "왼쪽 선택자"와 "오른쪽 선택자"를 만듭니다.
    # 초기에 "왼쪽 선택자"는 "중심 비교요소"를 제외한 범위의 가장 왼쪽 요소를, "오른쪽 선택자는" 범위의 가장 오른쪽 요소를 가리키게되고, 다음과 같은 루틴을 따릅니다
    left_cursor = pivot + 1
    right_cursor = end - 1

    # 0. 왼쪽 선택자와 오른쪽 선택자를 서로 비교하여, 검사 범위를 초과했는지 판별합니다.
    #    right_cursor는 오른쪽에서부터 "중앙 비교요소보다 작은 값", left_cursor는 왼쪽에서부터 "중앙 비교요소보다 큰 값"을 찾아나가게 되는데,
    #    왼쪽 선택자와 오른쪽 선택자가 같은 값이 된다면 이는 더 이상 왼쪽 선택자와 오른쪽 선택자 자리끼리 바꿀 요소가 없다는 것을 의미합니다
    #    유의!) 정렬 범위 크기가 2인 경우에도 초기 1회에 한해서 right_cursor를 설정할 필요가 있기 때문에 left_cursor < right_cursor가 아닌 left_cursor <= right_cursor를 작성했습니다
    while left_cursor <= right_cursor:
        # 주의) 아래 1번과 2번 과정을 진행할 때 당연하게도 왼쪽 선택자와 오른쪽 선택자가 정렬 범위 바깥을 나가면서까지 검사하지 않도록 처리를 해주어야 합니다

        # 1. 오른쪽 선택자는 "중심 비교요소"보다 더 낮은 값을 가진 값을 가리킬 때까지 왼쪽으로 이동합니다.
        # 주의) 오른쪽 연산자가 왼쪽의 끝까지 갈 때까지 단 한번도 "중앙 비교요소"보다 작은 요소를 가리키지 않는 상황이 발생할 수 있습니다.
        #       이럴 때 결국 right_cursor는 pivot과 같은 요소를 가리키게 되는데, 이 때 더이상 왼쪽으로 움직이지 않도록 처리해주어야 합니다
        #       이 이상 왼쪽으로 가면 정렬 범위를 벗어나게 되기 때문입니다
        while right_cursor > pivot and comparer(array[pivot], array[right_cursor]) == 1:
            right_cursor -= 1

        # 2. 왼쪽 선택자는 "중심 비교요소"보다 더 높은 값을 가진 값을 가리킬 때까지 오른쪽으로 이동합니다.
        #    또한 이동하다가 오른쪽 선택자와 같은 위치에 서게되면 이는 더이상 맞바꿀 값이 없다는 것을 의미하고, 오른쪽으로 이동하는 것을 중단합니다
        while left_cursor < end and left_cursor < right_cursor and comparer(array[pivot], array[left_cursor]) == -1:
            left_cursor += 1

        # 3. 왼쪽 선택자와 오른쪽 선택자가 서로 만나지 않았으면서 서로 값을 바꾸어야 하는 상황입니다
        #    왼쪽 선택자와 오른쪽 선택자가 가리키는 요소를 서로 맞바꿉니다
        if left_cursor < right_cursor:
            temp = array[left_cursor]
            array[left_cursor] = array[right_cursor]
            array[right_cursor] = temp
        # 4. 왼쪽 선택자와 오른쪽 선택자가 같은 요소를 가리키고 있다면 더 이상 맞바꿀 값은 없습니다
        #    각 선택자들의 이동을 멈춥니다
        else:
            break

    # 5. 위의 코드들을 거치고 나면 "오른쪽 선택자"는 "중앙 비교요소" 또는 "중앙 비교요소"보다 작은 요소를 가리키게 됩니다
    #    만약 "중앙 비교요소"를 가리키고 있는 것이 아니라면 "중앙 비교요소"와 "오른쪽 선택자"가 가리키는 값을 서로 맞바꿉니다
    #    이렇게 해야 비로소 "중앙 비교요소"를 기점으로 왼쪽에는 "중앙 비교요소"보다 작은 값들이, 오른쪽에는 "중앙 비교요소"보다 큰 값들이 위치하게 됩니다
    if pivot < right_cursor:
        temp = array[pivot]
        array[pivot] = array[right_cursor]
        array[right_cursor] = temp

        # "중앙 비교요소"는 이제 "오른쪽 선택자"가 가리키는 위치에 있습니다
        pivot = right_cursor

    # 6. "중앙 비교요소"를 기점으로 왼쪽 범위와 오른쪽 범위끼리 따로 정렬하도록 합니다
    quick_sort_inner(array, start, pivot, comparer)
    quick_sort_inner(array, pivot + 1, end, comparer)


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# 두 개의 점을 비교하여 어떤 것이 우선순위가 높은지 알려줍니다
# 왼쪽의 것이 높을 경우 -1을, 오른쪽이 높을 경우 1을 리턴합니다
def compare_dots(dot1, dot2):
    if dot1.y < dot2.y:
        return 1
    elif dot1.y > dot2.y:
        return -1
    elif dot1.x < dot2.x:
        return 1
    elif dot1.x > dot2.x:
        return -1
    else:
        return 0


dots_count = int(input())

dots_list = []

for i in range(0, dots_count):
    row_splitted = input().split()

    x = int(row_splitted[0])
    y = int(row_splitted[1])
    new_dot = Dot(x, y)

    dots_list.append(new_dot)

quick_sort(dots_list, compare_dots)

for dot in dots_list:
    print(dot.x, dot.y)