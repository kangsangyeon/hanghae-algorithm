import sys

person_count = int(sys.stdin.readline().rstrip())
row_splitted = sys.stdin.readline().rstrip().split()
person_list = [int(row_splitted[i]) for i in range(person_count)]

# 오름차순으로 정렬한 순서대로 기다리는 것이
# 사람들이 기다리는 시간의 총합이 가장 낮습니다
person_list.sort()

sum_of_whole_time = 0
required_time_to_work = 0
for person in person_list:
    required_time_to_work += person
    sum_of_whole_time += required_time_to_work

print(sum_of_whole_time)