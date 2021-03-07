alphabet_list = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def find_max_occurred_alphabet(string):

    max_occerrenced_char = "?"
    max_occerrenced_count = 0

    for alphabet in alphabet_list:
        occurrenced_count = 0
        for char in string:
            if alphabet == char:
                occurrenced_count += 1

        if max_occerrenced_count < occurrenced_count:
            max_occerrenced_count = occurrenced_count
            max_occerrenced_char = alphabet
        elif max_occerrenced_count == occurrenced_count:
            max_occerrenced_char = "?"

    return max_occerrenced_char


result = find_max_occurred_alphabet("hello my name is sparta")
print(result)
