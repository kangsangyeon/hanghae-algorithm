import sys

rows_count = int(sys.stdin.readline().rstrip())

for i in range(rows_count):
    input_row = sys.stdin.readline().rstrip()

    stack = 0
    is_vps = True

    for char in input_row:
        if char == "(":
            stack += 1
        elif char == ")":
            if stack == 0:
                is_vps = False
                break

            stack -= 1

    if stack > 0:
        is_vps = False

    if is_vps == True:
        print("YES")
    else:
        print("NO")