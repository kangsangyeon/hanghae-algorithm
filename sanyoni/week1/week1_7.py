def find_prime_list_under_number(number):
    not_prime_number_list = []
    prime_number_list = []

    for current_number in range(2, number + 1):
        if current_number not in not_prime_number_list:
            prime_number_list.append(current_number)

            multiple_of_current = current_number * 2
            while multiple_of_current <= number:
                not_prime_number_list.append(multiple_of_current)
                multiple_of_current += current_number

    return prime_number_list


input = 20

result = find_prime_list_under_number(input)
print(result)