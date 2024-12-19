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
print(result_dic)

# 1 2 3
# 2 3 4
# 4 5 6

# 9 8 7
# 8 7 6


result = 0
for k, v in result_dic.items():
    if v > 1:
        result += math.comb(v + 1, 2)
    elif v == 1:
        result += 1

print(result)
