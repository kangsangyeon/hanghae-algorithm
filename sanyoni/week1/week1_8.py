def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_of_character = [0] * 2
    for character in string:
        count_of_character[ord(character) - ord("0")] += 1

    minimum_count = count_of_character[0]
    if minimum_count > count_of_character[1]:
        minimum_count = count_of_character[1]

    return minimum_count


input = "011110"
result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)