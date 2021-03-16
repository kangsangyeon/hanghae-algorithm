# 숫자 안에 연속된 666이 있는지 확인합니다
def is_number_contains_666(number):
    while number >= 666:
        if number % 1000 == 666:
            return True

        number = number // 10

    return False


# N번째 영화의 제목에 들어간 수를 출력합니다
# 제목에 들어간 수는 666을 포함하는 N번째로 작은 수입니다
def solve(n):
    i = 666
    count = 0
    while True:
        if is_number_contains_666(i):
            count += 1

            if count == n:
                return i

        i += 1


input_n = int(input())
print(solve(input_n))
