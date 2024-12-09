import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()
lst = deque(lst)

mac_c = 0
while True:
    if len(lst) < 1:
        break
    l = lst.popleft()
    mac_c = max(mac_c, l * (len(lst) + 1))

print(mac_c)

"""
import sys

# import numpy as np


input = sys.stdin.readline
n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()
print(lst)

# max_c = 0
# for l in lst:
#     _lst = [l <= x for x in lst]
#     # print(_lst, sum(_lst))
#     c = l * sum(_lst)
#     max_c = max(max_c, c)
# print(max_c)

"""
