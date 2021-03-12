def is_group_word(word: str):
    already_exist_char_set = set()
    previous_char = ""
    for char in word:
        if char == previous_char:
            continue
        elif char not in already_exist_char_set:
            already_exist_char_set.add(char)
            previous_char = char
        else:
            return False

    return True


input_strings_count = int(input())

group_word_count = 0
for i in range(0, input_strings_count):
    is_group_word_flag = is_group_word(input())
    if is_group_word_flag == True:
        group_word_count += 1

print(group_word_count)

aabbcca