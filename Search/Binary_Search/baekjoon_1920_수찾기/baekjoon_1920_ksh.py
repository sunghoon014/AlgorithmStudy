import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
n_lst = list(map(int, input().split()))
n_lst.sort()

m = int(input())
m_lst = list(map(int, input().split()))

for m in m_lst:
    m_idx = bisect_left(n_lst, m)
    if m_idx < len(n_lst) and n_lst[m_idx] == m:
        print(1)
    else:
        print(0)
