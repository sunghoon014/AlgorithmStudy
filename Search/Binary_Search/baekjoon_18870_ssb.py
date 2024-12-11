from bisect import bisect_left

n = int(input())
data = list(map(int, input().split()))
data_sorted = sorted(set(data))

result = []
for i in range(n):
    result.append(bisect_left(data_sorted, data[i]))

print(*result)