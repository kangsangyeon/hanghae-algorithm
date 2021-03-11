stack = list()
stack_log_list = list()
push_index = 0


# 스택의 최상단에 수를 하나 더 쌓습니다
def stack_push():
    global stack, push_or_pop_list, push_index

    stack.append(push_index + 1)
    stack_log_list.append("+")
    push_index += 1


# 스택 최상단의 요소를 빼냅니다
def stack_pop():
    global stack, push_or_pop_list

    popped = stack.pop()
    stack_log_list.append("-")
    return popped


# 입력받을 숫자의 수입니다
input_count = int(input())

# 맨 처음 입력받은 숫자에 한해서,
# 별도 조건을 거치지 않고 stack에 입력받은 숫자만큼 push한 뒤
# pop함으로써 처리시간을 단축합니다
input_number = int(input())

for i in range(0, input_number):
    stack_push()

stack_pop()
# ###

for i in range(0, input_count - 1):
    input_number = int(input())

    if len(stack) == 0:
        stack_push()

    # 입력한 숫자에 다다를 때까지 stack을 하나 쌓습니다
    while stack[len(stack) - 1] < input_number:
        stack_push()

    # Error
    # 스택의 최상단의 수가 입력받은 수에 도달할 만큼 쌓아봤지만
    # 스택에 쌓인 최상위 수와 일치하지 않다면 표현이 불가능한 식입니다
    if stack[len(stack) - 1] > input_number or stack[len(stack) - 1] < input_number:
        print("NO")
        stack_log_list.clear()
        break

    # 입력한 숫자와 stack의 가장 최상위 숫자가 일치할 때 pop합니다
    stack_pop()

# 스택에 push 또는 pop한 기록을 출력합니다
for log in stack_log_list:
    print(log)