testcase_count = int(input())

for i in range(0, testcase_count):
    start, end = input().split()
    start = int(start)
    end = int(end)

    distance = end - start

    # 예외처리
    if distance <= 0:
        print(0)
    elif distance <= 1:
        print(1)
    else:
        boost_amount = 1
        boost_stack = 1
        while True:
            if distance >= boost_amount * 2:
                boost_stack += 1
                boost_amount += boost_stack
            else:
                boost_amount -= boost_stack
                boost_stack -= 1
                break

        count = 0
        remaining_distance = distance - (boost_amount * 2)
        if remaining_distance > boost_stack + 1:
            remaining_distance -= boost_stack + 1
            count += 1

        if remaining_distance > 0:
            count += 1

        print(boost_stack * 2 + count)