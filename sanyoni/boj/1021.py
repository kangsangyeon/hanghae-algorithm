max_number, number_count = input().split()
max_number = int(max_number)
number_count = int(number_count)

target_number_list = input().split()

# queue에 1부터 max_number까지 채웁니다
number_queue = list()
for i in range(0, max_number):
    number_queue.append(i + 1)

# 현재 queue의 어느 위치를 가르키고 있는지 저장하는 변수입니다
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