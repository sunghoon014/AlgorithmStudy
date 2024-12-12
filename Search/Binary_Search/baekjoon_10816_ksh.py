import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
n_lst = list(map(int, input().split()))
n_lst.sort()

m = int(input())
m_lst = list(map(int, input().split()))

result = []
for m in m_lst:
    m_left_idx = bisect_left(n_lst, m)
    m_right_idx = bisect_right(n_lst, m)
    result.append(str(m_right_idx - m_left_idx))
print(" ".join(result))
