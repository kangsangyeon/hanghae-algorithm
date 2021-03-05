import math

testcase_count = int(input())

for i in range(0, testcase_count):
    height, width, n = input().split()
    height = int(height)
    width = int(width)
    n = int(n)

    is_top_floor = (n % height) == 0
    if is_top_floor:
        y = height
    else:
        y = n % height

    x = math.ceil(n / height)

    print("{0}{1:02d}".format(y, x))
