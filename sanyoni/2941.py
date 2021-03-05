croatia_letter_alter_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]


# 매개변수로 전달한 문자열의 커서 위치에서부터
# 크로아티아 문자가 존재하는지 확인합니다
# 만약 크로아티아 문자가 존재한다면 크로아티아 문자를 표현하기 위해 사용하는 문자열 길이만큼 리턴하고,
# 크로아티아 문자가 존재하지 않는다면 0을 리턴합니다
# ex) is_croatia_alphabet("ljes=njak", 0) => 2
def is_croatia_alphabet(value, cursor):
    for croatia in croatia_letter_alter_list:
        temp = value[cursor : cursor + len(croatia)]
        if croatia == temp:
            return len(croatia)

    return 0


input_string = input()

# 문자의 개수를 저장하는 변수입니다.
# 프로그램 종료시 이 변수의 값을 출력할 것입니다
letter_count = 0

# 문자열의 어느 부분을 탐색중인지 저장하는 변수입니다
cursor = 0
while True:
    # 현재 위치에서 크로아티아 문자가 있는지 확인합니다
    # 크로아티아 문자가 있다면, 그 문자의 길이만큼 커서를 옮깁니다
    finded_croatia_letter_count = is_croatia_alphabet(input_string, cursor)
    if finded_croatia_letter_count > 0:
        cursor += finded_croatia_letter_count
    else:
        # 없다면 커서를 다음 위치로 옮깁니다
        cursor += 1

    # 옮긴 커서의 크기와 상관없이, 방금 탐색한 문자가 하나의 문자인 것이므로 문자 개수를 1 늘립니다
    letter_count += 1

    # 만약에 커서가 문자열의 끝에 도달했다면 탐색을 끝냅니다
    if cursor >= len(input_string):
        break

print(letter_count)