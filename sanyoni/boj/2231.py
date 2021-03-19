import sys

# 각 자리수를 더한 값을 반환하는 함수입니다
def get_sum_of_digits(number):
    sum_of_digit = 0
    while number > 0:
        sum_of_digit += number % 10
        number = number // 10

    return sum_of_digit


# 몇 자리 수인지에 대한 값을 반환하는 함수입니다
def get_digits_count(number):
    digits_count = 0
    while number > 0:
        digits_count += 1
        number = number // 10

    return digits_count


input_number = int(sys.stdin.readline().rstrip())
finded_value = 0

start = input_number - 10 * get_digits_count(input_number)
for i in range(start, input_number):
    sum_of_digit = get_sum_of_digits(i)
    temp = i + sum_of_digit
    if temp == input_number:
        finded_value = i
        break

print(finded_value)