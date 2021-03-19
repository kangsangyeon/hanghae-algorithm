input_string = input()


input_string_splitted = input_string.split("-")

# 처음으로 '-'기호가 나온 숫자들의 합을 구합니다
before_first_subtract_sum = 0
for number in input_string_splitted[0].split("+"):
    before_first_subtract_sum += int(number)

# 그 이후에 나온 모든 수들의 합을 구합니다
after_first_subtract_sum = 0
for temp in input_string_splitted[1:]:
    for number in temp.split("+"):
        after_first_subtract_sum += int(number)

# 처음으로 -가 나온 숫자들의 합에서 그 다음 나오는 모든 수를 빼면 정답이 됩니다
result = before_first_subtract_sum - after_first_subtract_sum
print(result)