import sys

input = sys.stdin.read
data = input().splitlines()
n = int(data[0])

ropes = [int(data[i]) for i in range(1, n + 1)]
ropes.sort(reverse=True)

max = ropes[0]
for i in range(1, n):
    weight = ropes[i] * (i + 1)
    if max < weight:
        max = weight

print(max)
