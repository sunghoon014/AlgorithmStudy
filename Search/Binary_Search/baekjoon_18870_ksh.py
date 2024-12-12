import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
n_lst = list(map(int, input().split()))
n_lst_sort = sorted(set(n_lst))

for n in n_lst:
    n_idx = bisect_left(n_lst_sort, n)
    print(n_idx, end=" ")
