# from bisect import bisect_left
# from collections import defaultdict

# n = int(input())
# a = list(map(int, input().split()))

# dict = defaultdict(int)
# for i in a:
#     dict[i] += 1
# # sorted_dict = {k: dict[k] for k in sorted(dict)}

# m = int(input())
# b = list(map(int, input().split()))

# result = []
# for j in b:
#     result.append(str(dict[j]))

# print(' '.join(result))

import bisect

n = int(input())
a = list(map(int, input().split()))
m = int(input())
data = list(map(int, input().split()))
a.sort()

result = []
for d in data:
    i = bisect.bisect_left(a, d)
    j = bisect.bisect_right(a, d)
    result.append(j-i)

print(*result)