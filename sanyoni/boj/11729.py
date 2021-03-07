# 하노이의 탑에는 원판을 높을 수 있는 장대 세 개가 있습니다
# 이 프로그램에서는 각 장대에 1번부터 3번까지 번호를 붙여 처리합니다
# count: 옮길 원판의 개수를 의미합니다
# start: 옮길 원판들이 있는 장대의 위치입니다
# end: 옮길 원판들이 이동될 목적지 장대의 위치입니다
def hanoi(count: int, start: int, to: int):
    if count == 1:
        print(start, to)
        return

    # 원판들을 한 번에 옮길 수 없으니 "가장 밑의 원판"이 아닌 나머지 원판들을 목적지가 아닌 다른 장대에 옮길 필요가 있습니다
    # 이 변수값은 그 나머지 원판들이 먼저 옮겨져야 할 다른 장대의 위치값입니다
    bypass = 6 - (start + to)

    # 가장 밑의 원판을 제외한 나머지 원판들을
    # "중간에 거쳐갈 곳"으로 옮깁니다.
    hanoi(count - 1, start, bypass)

    # 가장 밑의 원판을 목적지로 보냅니다
    print(start, to)

    # 가장 밑에 원판을 목적지로 이동했으니,
    # 아까 "중간에 거쳐갈 곳"으로 이동했던 원판들을 목적지로 보냅시다!
    hanoi(count - 1, bypass, to)


obj_count = int(input())

# 실행 횟수를 출력합니다
proceed_count = pow(2, obj_count) - 1
print(proceed_count)

# 초기에 모든 원판은 1번 장대에 모여있다고 가정되어 있습니다
# 이 모든 원판들을 3번 장대에 옮깁니다
hanoi(obj_count, 1, 3)