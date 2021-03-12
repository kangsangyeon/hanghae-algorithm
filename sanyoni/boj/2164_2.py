from collections import deque

cards_count = int(input())

# 예외
# 카드가 한 장인 경우 무조건 1이 출력됩니다
# 이 예외처리는 카드가 한 장일 때 pop하지 않도록 하기 위함입니다
if cards_count == 1:
    print(1)
else:
    # 카드 목록을 추가합니다
    queue = deque(list(range(1, cards_count + 1)))

    # 카드를 빼고, 뒤로 넣는 동작을 반복합니다.
    # 카드를 뺀 직후에 카드가 한 장 남았다면, 그 한장을 출력합니다
    while True:
        queue.popleft()

        if len(queue) == 1:
            print(queue.pop())
            break
        else:
            temp = queue.popleft()
            queue.append(temp)