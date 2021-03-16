import sys

numbers_list = []
numbers_count_dict = dict()
average_of_numbers = 0
sum_of_numbers = 0


numbers_count = int(sys.stdin.readline())
for i in range(numbers_count):
    input_number = int(sys.stdin.readline())

    numbers_list.append(input_number)

    if input_number not in numbers_count_dict:
        numbers_count_dict[input_number] = 1
    else:
        numbers_count_dict[input_number] += 1

    sum_of_numbers += input_number

numbers_list.sort()

# 평균값을 구합니다
average_of_numbers = sum_of_numbers / numbers_count

# 중앙값을 구합니다
middle_index = numbers_count // 2
middle_value = numbers_list[middle_index]

# 최빈값을 구합니다
max_mode_count = 0
max_mode_numbers_list = []

for key in numbers_count_dict.keys():
    number_count = numbers_count_dict[key]

    if max_mode_count == number_count:
        max_mode_numbers_list.append(key)

    elif max_mode_count < number_count:
        max_mode_numbers_list.clear()
        max_mode_numbers_list.append(key)

        max_mode_count = number_count

# 입력받은 숫자들을 전부 포함하는 범위의 크기를 구합니다
number_range = 0
number_range = numbers_list[len(numbers_list) - 1] - numbers_list[0]

print(round(average_of_numbers))
print(middle_value)

if len(max_mode_numbers_list) == 1:
    print(max_mode_numbers_list[0])
else:
    max_mode_numbers_list.sort()
    print(max_mode_numbers_list[1])

print(number_range)