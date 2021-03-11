max_number, number_count = input().split()
max_number = int(max_number)
number_count = int(number_count)

target_number_list = input().split()

# 1부터 입력받은 숫자까지 저장되어있는 queue에서
# 원하는 원소들을 순서대로 빼내기 위해 최소한 얼만큼의 원소 이동이 필요한지 계산하는 프로그램입니다.
# 이 코드에서는 최적화를 위해 "물리적으로 모든 원소들을 한 칸만큼 오른쪽/왼쪽으로 이동"하는 것을
# 커서 이동으로 대체하여 논리적으로 queue를 구현했습니다.
# 커서는 queue의 맨 앞 요소를 가르키는 변수입니다
# 모든 원소들은 1부터 차례대로 아래에 추가된다고 가정합니다.
# 입력 예:
#   10 3
#
# 1부터 10까지, 총 10개의 원소를 가지고 있는 queue는 프로그램 초기에 다음과 같이 초기화됩니다
# 맨 처음에 cursor는 가장 먼저 추가된 요소를 가르키고 있습니다. 따라서 초기 값은 queue의 최상단 인덱스값인 0입니다
#
# queue: 1   <- cursor
#        2
#        3
#        .
#        .
#        .
#        10

# queue에 1부터 max_number까지 채웁니다
number_queue = list()
for i in range(0, max_number):
    number_queue.append(i + 1)

# 현재 queue의 맨 앞 요소의 위치입니다
# 모든 원소들을 오른쪽/왼쪽으로 이동할 때마다 이 값이 변경됩니다
cursor = 0

# 몇 번 움직였는지 합계를 누적하는 변수입니다
total_step_count = 0

for target_number in target_number_list:

    target_number = int(target_number)

    # 목표 숫자가 큐의 어느 위치에 있는지 확인합니다
    target_index = 0
    for i in range(0, len(number_queue)):
        if number_queue[i] == target_number:
            target_index = i
            break

    # 그 위치로 가기 위해 위 또는 아래방향 둘 중 어느 방향으로 이동하는게 효율적인지 판단합니다
    # directionY는 단순히 디버깅용 변수로, 이 값이 1이라면 아래쪽으로 이동하고
    # 이 값이 -1이라면 위쪽으로 이동한다는 것을 알 수 있도록 했습니다
    # minimum_step_to_reach는 목표 위치로 이동하기 위해서 필요한 최소한의 움직임 횟수로 설정됩니다
    max_index = len(number_queue) - 1

    directionY = 0
    minimum_step_to_reach = 0

    if cursor < target_index:
        if target_index - cursor < (max_index - target_index) + cursor + 1:
            directionY = 1
            minimum_step_to_reach = target_index - cursor
        else:
            directionY = -1
            minimum_step_to_reach = (max_index - target_index) + cursor + 1
    elif cursor > target_index:
        if cursor - target_index < (max_index - cursor) + target_index + 1:
            directionY = -1
            minimum_step_to_reach = cursor - target_index
        else:
            directionY = 1
            minimum_step_to_reach = (max_index - cursor) + target_index + 1
    else:
        pass

    # 커서를 옮기고 그 커서위치에 있는 원소를 삭제합니다
    cursor = target_index
    number_queue.pop(cursor)

    # 몇 칸 움직였는지 누적합니다
    total_step_count += minimum_step_to_reach

print(total_step_count)