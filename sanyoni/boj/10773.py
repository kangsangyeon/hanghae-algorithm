import sys

stack = []

input_count = int(sys.stdin.readline())
sum_of_number = 0

for i in range(input_count):
    input_number = int(sys.stdin.readline())
    if input_number == 0:
        popped = stack.pop()
        sum_of_number -= popped
        continue

    stack.append(input_number)
    sum_of_number += input_number

print(sum_of_number)