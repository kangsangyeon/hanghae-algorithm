import sys


def binary_search(array, target):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
            continue

        elif array[mid] > target:
            end = mid - 1
            continue

        else:
            return 1

    return 0


exist_numbers_count = int(sys.stdin.readline().rstrip())
exist_numbers_list = [int(value) for value in sys.stdin.readline().rstrip().split()]

search_numbers_count = int(sys.stdin.readline().rstrip())
search_numbers_list = [int(value) for value in sys.stdin.readline().rstrip().split()]

exist_numbers_list.sort()

for value in search_numbers_list:
    print(binary_search(exist_numbers_list, value))