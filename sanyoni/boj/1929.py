# Hint) 에라토스테네스의 체를 검색해보면 좋습니다
# https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4

minimum, maximum = input().split()
minimum = int(minimum)
maximum = int(maximum)

# 소수가 아닌 수들의 집합입니다
# 2부터 시작하여 숫자를 하나씩 증가시키며 이 집합에 없는 수는 출력하고,
# 그 수의 배수들을 이 집합에 모두 추가합니다
not_prime_number_set = set()

# 소수의 배수들을 걸러내는 작업은 가장 작은 소수값부터 시작해야 올바른 결과가 나옵니다
# 따라서 반복문의 index를 minimum이 아닌 2부터 시작해야 합니다
for i in range(2, maximum + 1):
    if i not in not_prime_number_set:
        # 출력하기 위한 최소 수는 minimum 입니다
        if i >= minimum:
            print(i)

        # 이 수의 배수들은 소수가 아닙니다
        # 이 수의 배수들을 모두 not_prime_number_set에 추가합니다
        j = i * 2
        while j <= maximum:
            not_prime_number_set.add(j)
            j = j + i