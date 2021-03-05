testcase_count = int(input())

for i in range(0, testcase_count):
    # 입력받은 줄을 공백으로 나눕니다
    # row_splitted는 공백으로 나뉜 요소들의 리스트로 초기화됩니다
    row = input()
    row_splitted = row.split(" ")

    # 학생의 수는 각 줄의 0번째 요소에 있습니다
    student_count = int(row_splitted[0])

    # "모든 학생의 점수를 더한 결과"를 얻습니다
    all_score = 0
    for j in range(0, student_count):
        all_score += int(row_splitted[j + 1])

    # "모든 학생의 평균 점수"를 얻습니다
    everage_score = all_score / student_count

    # "평균 점수 이상의 점수를 획득한 학생들의 수"를 얻습니다
    over_everage_student_count = 0
    for j in range(0, student_count):
        if int(row_splitted[j + 1]) > everage_score:
            over_everage_student_count += 1

    # "평균 점수 이상의 점수를 획득한 학생들의 수"는 전체 학생 중 어느정도 비율인지 계산하고, 그 후 출력합니다
    # 출력할 때 백분율(%)로 나타낼 수 있도록 formatting합니다
    over_everage_rate = over_everage_student_count / student_count
    print(format(over_everage_rate, "0.3%"))
