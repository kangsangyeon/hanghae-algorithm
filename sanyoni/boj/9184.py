precalculated_w_dict = dict()


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if a < b and b < c:
        if (a, b, c) in precalculated_w_dict:
            return precalculated_w_dict[(a, b, c)]
        else:
            value = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
            precalculated_w_dict[(a, b, c)] = value
            return value

    else:
        if (a, b, c) in precalculated_w_dict:
            return precalculated_w_dict[(a, b, c)]
        else:
            value = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
            precalculated_w_dict[(a, b, c)] = value
            return value


while True:
    input_string_splitted = input().split()
    number_a = int(input_string_splitted[0])
    number_b = int(input_string_splitted[1])
    number_c = int(input_string_splitted[2])

    # 종료 조건입니다
    if number_a == -1 and number_b == -1 and number_c == -1:
        break

    w_value = w(number_a, number_b, number_c)

    print(f"w({number_a}, {number_b}, {number_c}) = {w_value}")
