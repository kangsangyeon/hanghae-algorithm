def quick_sort(array):
    quick_sort_inner(array, 0, len(array))


def quick_sort_inner(array, start, end):
    if (end - start) <= 1:
        return

    pivot = start

    left_cursor = pivot + 1
    right_cursor = end - 1

    while left_cursor <= right_cursor:
        while right_cursor > pivot and array[right_cursor] > array[pivot]:
            right_cursor -= 1

        while left_cursor < end and left_cursor < right_cursor and array[left_cursor] < array[pivot]:
            left_cursor += 1

        if left_cursor < right_cursor:
            array[left_cursor], array[right_cursor] = array[right_cursor], array[left_cursor]
        else:
            break

    if pivot < right_cursor:
        array[pivot], array[right_cursor] = array[right_cursor], array[left_cursor]

    quick_sort_inner(array, start, pivot)
    quick_sort_inner(array, pivot + 1, end)


numbers_list = []

input_numbers_count = int(input())
for i in range(0, input_numbers_count):
    number = int(input())
    numbers_list.append(number)

quick_sort(numbers_list)

for number in numbers_list:
    print(number)