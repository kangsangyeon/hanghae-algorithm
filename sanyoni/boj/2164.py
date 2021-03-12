cards_list = []
cursor = 0

cards_count = int(input())


# 예외
# 카드가 한 장인 경우 무조건 1이 출력됩니다
# 이 예외처리는 카드가 한 장일 때 pop하지 않도록 하기 위함입니다
if cards_count == 1:
    print(1)
else:
    # 카드 목록을 추가합니다
    for i in range(0, cards_count):
        cards_list.append(i + 1)

    while True:
        cards_list.pop(cursor)

        cursor = (cursor + 1) % len(cards_list)

        if len(cards_list) == 1:
            print(cards_list[0])
            break