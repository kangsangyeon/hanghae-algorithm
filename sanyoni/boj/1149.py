# 집의 개수와 각 집을 칠하는 비용 리스트를 초기화합니다
house_count = int(input())
house_cost = [[0 for col in range(3)] for row in range(house_count)]

for i in range(0, house_count):
    row_splitted = input().split()
    house_cost[i][0] = int(row_splitted[0])
    house_cost[i][1] = int(row_splitted[1])
    house_cost[i][2] = int(row_splitted[2])

# 최적의 비용을 찾고 누적해나갑니다.
house_cost_dp = [[0 for col in range(3)] for row in range(house_count)]

house_cost_dp[0][0] = house_cost[0][0]
house_cost_dp[0][1] = house_cost[0][1]
house_cost_dp[0][2] = house_cost[0][2]

for i in range(1, house_count):
    house_cost_dp[i][0] = min(house_cost_dp[i - 1][1], house_cost_dp[i - 1][2]) + house_cost[i][0]
    house_cost_dp[i][1] = min(house_cost_dp[i - 1][0], house_cost_dp[i - 1][2]) + house_cost[i][1]
    house_cost_dp[i][2] = min(house_cost_dp[i - 1][0], house_cost_dp[i - 1][1]) + house_cost[i][2]

# 최적의 비용은 house_cost_dp의 마지막 배열 중 가장 값이 낮은 요소값입니다
min_cost = min(house_cost_dp[house_count - 1][0], house_cost_dp[house_count - 1][1], house_cost_dp[house_count - 1][2])

# 최적의 비용출력합니다.
print(min_cost)