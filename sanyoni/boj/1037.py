numbers_count = int(input())
rows_splitted = input().split()
numbers_list = list([int(value) for value in rows_splitted])
numbers_list.sort()

print(numbers_list[0] * numbers_list[len(numbers_list) - 1])