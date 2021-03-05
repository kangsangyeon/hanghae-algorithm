# 각 자리수의 총합을 반환하는 함수입니다
# get_sum_of_digit(12345) => 1 + 2 + 3 + 4 + 5 = 15
def get_sum_of_digit(number):
    leftover_value = number
    sum_of_digit = 0
    while True:
        digit_of_first = int(leftover_value % 10)

        sum_of_digit += digit_of_first

        leftover_value = leftover_value / 10
        if leftover_value < 1:
            break

    return sum_of_digit


# n과 n의 각 자리수를 더하는 함수입니다
# ex) d(75) = 75 + 7 + 5 = 87
def d(number):
    return number + get_sum_of_digit(number)


# 셀프 넘버가 아닌 숫자들의 모임입니다.
# 아래에서 for문을 순회하며 생성자를 가지고 있는 숫자들이 여기에 추가됩니다
# for문을 순회하며 1이상 10000미만의 숫자들을 비교해가며 이 리스트 안에 없을 경우,
# 그 값은 생성자가 없는 숫자, 즉 셀프 넘버이므로 그 수를 출력합니다
not_self_number_list = []

for i in range(1, 10000):
    current_not_self_number = d(i)

    not_self_number_list.append(current_not_self_number)

    # 셀프 넘버가 아닌 리스트에 없습니다
    # 이 수(i)는 셀프 넘버입니다
    if i not in not_self_number_list:
        print(i)