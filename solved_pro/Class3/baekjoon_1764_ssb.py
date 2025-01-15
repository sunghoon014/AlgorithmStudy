import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
dict = defaultdict(int)
for i in range(n+m):
    name = input().strip()
    dict[name] += 1

result = []
for k, v in dict.items():
    if v==2:
        result.append(k)
result.sort()
print(len(result))
for r in result:
    print(r)