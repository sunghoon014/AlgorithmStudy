from collections import defaultdict

n, c = map(int, input().split())
data = list(map(int, input().split()))

dict = defaultdict(int)
for num in data:
    dict[num] += 1
dict_sorted = {k: dict[k] for k in sorted(dict, key=lambda k: -dict[k])}

result = []
for i, j in dict_sorted.items():
    for _ in range(j):
        result.append(i)

print(*result)