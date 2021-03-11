# fibonaci(n)의 값을 O(1)으로 가져올 수 있도록
# fibonaci 함수의 값들을 미리 계산한 딕셔너리를 만들고 초기화합니다
fibonaci_dict = {0: 0, 1: 1, 2: 1}
for i in range(3, 41):
    fibonaci_dict[i] = fibonaci_dict[i - 1] + fibonaci_dict[i - 2]


testcase_count = int(input())
for i in range(0, testcase_count):
    number = int(input())

    # fibonaci(N)을 호출할 때
    # 재귀적으로 호출되는 fibonaci(0)과 fibonaci(1)의 호출 횟수는
    # 각각 fibonaci(N-1)번, fibonaci(N)번입니다
    # 예외) fibonaci(0)일 때 호출되는 횟수는 각각 1, 0번입니다.
    # 이 경우 fibonaci(N-1) 값을 사용할 수 없기 때문에 예외로 상수를 건네주어야 합니다
    if number == 0:
        print("1 0")
    else:
        print(fibonaci_dict[number - 1], fibonaci_dict[number])