positive_number_sorted_list = []
negative_number_sorted_list = []

# 입력받은 숫자들을 토대로 양수와 음수를 분리하여 저장하는 리스트를 만듭니다
# 양수는 양수끼리, 음수는 음수끼리 곱하여 곱의 크기를 최대화하려는 목적입니다
# 유의) 0은 음수의 리스트에 추가합니다. 0과 음수를 곱하여 음수를 없애려는 목적입니다
input_count = int(input())
for i in range(0, input_count):
    number = int(input())

    if number > 0:
        positive_number_sorted_list.append(number)
    elif number <= 0:
        negative_number_sorted_list.append(number)

positive_number_sorted_list.sort()
negative_number_sorted_list.sort(reverse=True)

result = 0

while len(positive_number_sorted_list) > 0:
    first_number = positive_number_sorted_list.pop()

    if len(positive_number_sorted_list) > 0:
        second_number = positive_number_sorted_list.pop()

        if first_number == 1 or second_number == 1:
            result += first_number + second_number
        else:
            result += first_number * second_number
    else:
        result += first_number

while len(negative_number_sorted_list) > 0:
    first_number = negative_number_sorted_list.pop()

    if len(negative_number_sorted_list) > 0:
        second_number = negative_number_sorted_list.pop()

        result += first_number * second_number
    else:
        result += first_number

print(result)