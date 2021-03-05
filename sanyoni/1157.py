input_string = input()

# 각 알파벳들이 문자열 안에 몇 개 있는지 세는 리스트입니다
# ex) 알파벳 'c'가 문자열 내에 몇 개 있는지에 대한 값은
# alphabet_count_list[ord("c") - ord("a")]로 가져올 수 있습니다
#   *ord() 함수는 문자의 아스키 코드 값을 리턴합니다
alphabet_count_list = [0] * 26

# 문자열 내에 가장 많이 포함되는 알파벳과 그 개수를 저장하는 변수입니다
# 이는 프로그램 종료 직전에 출력하는 값이기도 합니다
max_count_alphabet = 0
max_count = 0

# 문자열 내를 순회하며 알파벳 개수를 늘리고,
# 가장 많이 포함되어있는 알파벳과 그 개수를 설정합니다
for i in range(0, len(input_string)):
    current_alphabet = input_string[i].upper()
    current_alphabet_index = ord(current_alphabet) - ord("A")

    alphabet_count_list[current_alphabet_index] += 1

    if alphabet_count_list[current_alphabet_index] > max_count:
        max_count = alphabet_count_list[current_alphabet_index]
        max_count_alphabet = current_alphabet

# 가장 많이 포함되어 있는 알파벳은 여러 개일 수 있습니다.
# 각 알파벳 개수를 저장하는 리스트를 순회하며 이를 검사합니다
# 만약 그렇다면, 출력값을 ?로 하기 위해 max_count_alphabet을 "?"로 설정합니다
# ex) Mississipi 에서 s와 i는 4개씩 들어가 있으므로, 출력값을 ?로 합니다
for i in range(0, len(alphabet_count_list)):
    another_max_count_of_alphabet = alphabet_count_list[i] >= max_count
    another_max_count_of_alphabet &= ord("A") + i is not ord(max_count_alphabet)
    if another_max_count_of_alphabet:
        max_count_alphabet = "?"
        break

# 문자열 내에 가장 많이 포함되어있는 알파벳을 출력합니다
print(max_count_alphabet)