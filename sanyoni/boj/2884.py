hour, minute = input().split()
hour = int(hour)
minute = int(minute)

# minute이 45 이상이면, 시간이 지난 시간으로 넘어가지 않아도 됩니다.
if minute >= 45:
    minute = minute - 45
else:
    # 시간이 음수라면, 자정 전(0시)이니 23시로 돌아갑니다
    hour = hour - 1
    if hour < 0:
        hour = 23

    # 위의 계산과 아래의 계산의 결과는 완전 동일합니다
    # minute = 60 - (45 - minute)
    minute = 15 + minute

print(hour, minute)