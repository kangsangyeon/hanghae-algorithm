import sys


def permutation(target_depth, end):
    for i in range(1, end + 1):
        permutation_array = []
        permutation_inner(target_depth, 1, i, end, permutation_array)


def permutation_inner(target_depth, current_depth, start, end, array: list):
    if start > end:
        return

    if current_depth == target_depth:
        print(*array, start)
        return

    for i in range(start, end + 1):
        array.append(start)
        permutation_inner(target_depth, current_depth + 1, i + 1, end, array)
        array.pop()


end, permutation_depth = sys.stdin.readline().rstrip().split()
end = int(end)
permutation_depth = int(permutation_depth)

permutation(permutation_depth, end)