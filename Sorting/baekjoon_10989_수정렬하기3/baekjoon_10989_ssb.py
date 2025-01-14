# from collections import defaultdict
# import sys
# input = sys.stdin.readline
# n = int(input())

# dict = defaultdict(int)
# for _ in range(n):
#     data = int(input())
#     dict[data] += 1

# dict = {k: dict[k] for k in sorted(dict)}
# for i in dict.keys():
#     for j in range(dict[i]):
#         print(i)


import sys
from collections import defaultdict

input = sys.stdin.readline
dict = defaultdict(int)

n = int(input())
for _ in range(n):
    data = int(input())
    dict[data] += 1

dict = {k: dict[k] for k in sorted(dict)}
for key, value in dict.items():
    for v in range(value):
        print(key)