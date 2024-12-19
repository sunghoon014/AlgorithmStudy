import sys

N, C = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers_dict = dict()

for number in numbers:
    if number in numbers_dict:
        numbers_dict[number] += 1
    else:
        numbers_dict[number] = 1

sorted_dict = sorted(numbers_dict.items(), reverse=True, key=lambda x:x[1])

res = []
for num, count in sorted_dict:
    for i in range(count):
        res.append(num)

print(*res)