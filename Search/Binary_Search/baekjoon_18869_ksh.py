import sys
from bisect import bisect_left
import math

input = sys.stdin.readline

M, N = map(int, input().split())

result_dic = {}
for _ in range(M):
    n = list(map(int, input().split()))
    n_ordered = sorted(n)
    n_idx = [bisect_left(n_ordered, x) for x in n]
    try:
        result_dic[str(n_idx)] += 1
    except:
        result_dic[str(n_idx)] = 0

result = 0
for k, v in result_dic.items():
    if v > 1:
        result += math.comb(v + 1, 2)
    elif v == 1:
        result += 1

print(result)
