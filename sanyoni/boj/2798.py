import sys

# 주어진 배열 안에서 카드 3장을 뽑았을 때 얻을 수 있는 조합의 값 중 가장 목표치에 근접한 값을 얻는 함수입니다
def find_best_adjacent_combination(numbers_list: list[int], target_number: int, max_depth: int, current_depth: int, best_combination_sum: list[int], current_combination_sum: int, start: int):
    # 카드 3장을 뽑았다면 이 조합이 지금까지 발견한 조합들 중 가장 큰 수인지 확인하고,
    # 만약 그렇다면 최고의 조합의 합을 갱신합니다
    if current_depth >= max_depth:
        if current_combination_sum > best_combination_sum[0]:
            best_combination_sum[0] = current_combination_sum

        return

    if start >= len(numbers_list):
        return

    for i in range(start, len(numbers_list)):
        # 현재 수들의 조합이 "목표하는 수치"보다 같거나 작은지를 판별합니다
        if current_combination_sum + numbers_list[i] <= target_number:
            find_best_adjacent_combination(numbers_list, target_number, max_depth, current_depth + 1, best_combination_sum, current_combination_sum + numbers_list[i], i + 1)
        # 현재 수들의 조합이 "목표하는 수치"보다 크다면, 그 뒤에 있는 요소들 모두 클 것이므로
        # 더 이상 비교하지 않고 이번에 조합하던 수를 포기합니다
        else:
            break


# main
numbers_count, target_number = sys.stdin.readline().rstrip().split()
numbers_count = int(numbers_count)
target_number = int(target_number)

row_splitted = sys.stdin.readline().rstrip().split()
numbers_list = [int(value) for value in row_splitted]
numbers_list.sort()

# 3개의 숫자들의 조합 중 최고의 조합의 합을 저장하는 리스트입니다
# 함수 호출시에 레퍼런스를 건네주기 위해 리스트로 만들었으며,
# 리스트로서의 기능보다 정수형 포인터 변수같은 느낌으로 사용합니다
best_combination_sum = [0]

find_best_adjacent_combination(numbers_list, target_number, 3, 0, best_combination_sum, 0, 0)

print(best_combination_sum[0])