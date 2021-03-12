import math

MAX_NUMBER_RANGE = 123456 * 2
not_prime_number_set = set()
not_prime_number_set.add(1)

# 소수가 아닌 수들의 집합을 초기화합니다
for i in range(2, int(math.sqrt(MAX_NUMBER_RANGE))):
    if i not in not_prime_number_set:
        j = i * i
        not_prime_number_set.add(j)

        while j <= MAX_NUMBER_RANGE:
            j += i
            not_prime_number_set.add(j)

while True:
    input_number = int(input())

    # 종료 조건입니다
    if input_number == 0:
        break

    # n < prime <= n * 2 범위의 소수가 몇 개인지 누적하고 출력합니다
    prime_number_in_range_count = 0
    for i in range(input_number + 1, input_number * 2 + 1):
        if i not in not_prime_number_set:
            prime_number_in_range_count += 1

    print(prime_number_in_range_count)