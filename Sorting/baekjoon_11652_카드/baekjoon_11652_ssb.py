from collections import defaultdict

n = int(input())

dict = defaultdict(int)
for _ in range(n):
    data = int(input())
    dict[data] += 1

dict = sorted(dict.items(), key=lambda x: (-x[1], x[0]))
print(dict[0][0])