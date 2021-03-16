input_height = int(input())

# 정수 삼각형을 초기화합니다
values = [[-1 for col in range(input_height)] for row in range(input_height)]
for row in range(0, input_height):
    input_row_splitted = input().split()
    for col in range(0, row + 1):
        values[row][col] = int(input_row_splitted[col])

# 정수 삼각형을 위에서부터 내려오면서 각 경로에 대한 가중치를 누적한 배열입니다
max_route_dp = [[-1 for col in range(input_height)] for row in range(input_height)]

max_route_dp[0][0] = values[0][0]

for row in range(1, input_height):
    max_route_dp[row][0] = max_route_dp[row - 1][0] + values[row][0]
    max_route_dp[row][row] = max_route_dp[row - 1][row - 1] + values[row][row]

    for col in range(1, row):
        max_route_value = max(max_route_dp[row - 1][col - 1], max_route_dp[row - 1][col])
        max_route_dp[row][col] = max_route_value + values[row][col]

max_route_value = max(max_route_dp[input_height - 1])

print(max_route_value)