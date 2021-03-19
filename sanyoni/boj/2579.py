import sys

# 입력을 받습니다
stairs_count = int(sys.stdin.readline().rstrip())
stairs_list = [0] * (stairs_count + 1)
for i in range(0, stairs_count):
    stairs_list[i + 1] = int(sys.stdin.readline().rstrip())

# 점화식으로 값을 얻어내기 전에 초기항을 초기화해줍니다
stairs_dp = [0] * (stairs_count + 1)
stairs_dp[0] = 0

if stairs_count >= 1:
    stairs_dp[1] = stairs_list[1]

if stairs_count >= 2:
    stairs_dp[2] = stairs_list[1] + stairs_list[2]

# 점화식으로 나머지 "계단별로 그 계단까지 올라갔을 때까지 얻을 수 있는 최고점수"를 얻어냅니다
for i in range(3, len(stairs_dp)):
    one_step = stairs_dp[i - 3] + stairs_list[i - 1] + stairs_list[i]
    two_step = stairs_dp[i - 2] + stairs_list[i]

    stairs_dp[i] = max(one_step, two_step)

print(stairs_dp[len(stairs_dp) - 1])