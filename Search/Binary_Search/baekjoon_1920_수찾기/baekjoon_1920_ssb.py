# import bisect

# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# b = list(map(int, input().split()))

# a.sort()
# for i in range(m):
#     temp = bisect.bisect_left(a, b[i])
#     try:
#         if a[temp]==b[i]:
#             print(1)
#         else:
#             print(0)
#     except IndexError:
#         print(0)

import bisect

n = int(input())
a = list(map(int, input().split()))
m = int(input())
data = list(map(int, input().split()))
a.sort()

for d in data:
    i = bisect.bisect_left(a, d)
    if i < n and a[i] == d:
        print(1)
    else:
        print(0)