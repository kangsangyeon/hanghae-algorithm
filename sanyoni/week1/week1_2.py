input = "hello my name is sparta"


def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if char.isalpha() is False:
            continue

        alphabet_index = ord(char) - ord("a")
        alphabet_occurrence_array[alphabet_index] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))