import sys
input = sys.stdin.readline
from collections import Counter

N, C = map(int, input().split())
msg = list(map(int, input().split())) #2 1 2 1 2

msg_cnt = Counter(msg)
print(msg_cnt) #Counter({2: 3, 1: 2})

idx = {}

for i, x in enumerate(msg):
    if x not in idx:
        idx[x] = i
print(idx) #{2: 0, 1: 1}

sort = sorted(msg_cnt.keys(), key = lambda x : (-msg_cnt[x], idx[x]))
print(sort) # [2, 1]
result = []
for num in sort:
    result.extend([num] * msg_cnt[num])
    
print(*result)
