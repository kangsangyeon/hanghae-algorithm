value = int(input())
origin_value = value

iterated_count = 0
while True:
    calculated_value = int(value / 10) + (value % 10)
    value = ((value % 10) * 10) + (calculated_value % 10)
    iterated_count += 1

    if value is origin_value:
        break

print(iterated_count)