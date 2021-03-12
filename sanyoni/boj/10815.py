# 배열을 이진 탐색하여 값의 존재 여부를 리턴합니다
def binary_search(array, value):
    range_start = 0
    range_end = len(array) - 1

    cursor = (range_start + range_end) // 2

    while range_start < range_end:
        cursor = (range_start + range_end) // 2

        if value > array[cursor]:
            range_start = cursor + 1
        elif value < array[cursor]:
            range_end = cursor - 1
        else:
            return True

    cursor = range_start

    if array[cursor] == value:
        return True
    else:
        return False


own_cards_list = []
is_exist_card_string = ""

# 상근이가 가지고 있는 카드를 입력받고,
# 이분탐색할 수 있도록 정렬합니다
input_own_cards_count = int(input())
input_own_cards_row_splitted = input().split()
for item in input_own_cards_row_splitted:
    own_cards_list.append(int(item))

own_cards_list.sort()

# 가지고 있는지 비교할 카드들을 입력받고
# 이를 한 번에 출력할 수 있도록 비교한 이력들을 하나의 문자열로 만듭니다
input_compare_cards_count = int(input())
input_compare_cards_splitted = input().split()
for item in input_compare_cards_splitted:
    card = int(item)

    is_exist_card = binary_search(own_cards_list, card)

    is_exist_card_01 = "0"
    if is_exist_card == True:
        is_exist_card_01 = "1"

    if is_exist_card_string == "":
        is_exist_card_string = is_exist_card_01
    else:
        is_exist_card_string += " " + is_exist_card_01

print(is_exist_card_string)