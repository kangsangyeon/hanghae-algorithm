import math

A, B, V = input().split()
A = int(A)
B = int(B)
V = int(V)

# 달팽이가 정상에 도달하지 못했을 경우, 달팽이가 하루동안 올라가는 높이입니다
length_per_date = A - B

# "달팽이가 하루 안에 올라갈 수 있는 위치"입니다
almost_arrived_position = V - A

# 달팽이가 하루 만에 올라갈 수 있는 위치에 도달하기까지 걸리는 날입니다
days_count_to_almost_arrived = math.ceil(almost_arrived_position / length_per_date)

print(days_count_to_almost_arrived + 1)