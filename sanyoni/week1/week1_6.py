input = "abacabade"


def find_not_repeating_character(string):
    already_finded_character_list = []
    not_repeated_character_list = []

    for character in string:
        if character in already_finded_character_list:
            if character in not_repeated_character_list:
                not_repeated_character_list.remove(character)
            continue
        else:
            already_finded_character_list.append(character)
            not_repeated_character_list.append(character)

    result = "_"
    if len(not_repeated_character_list) > 0:
        result = not_repeated_character_list[0]

    return result


result = find_not_repeating_character(input)
print(result)