n, x = map(int, input().split())
data = list(map(int, input().split()))

result = []
for i in data:
    if i<x:
        result.append(i)

print(*result)