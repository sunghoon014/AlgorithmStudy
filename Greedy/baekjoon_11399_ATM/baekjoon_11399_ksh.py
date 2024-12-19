import sys

input = sys.stdin.readline
n = int(input())
line = list(map(int, input().split()))
line.sort()

result = []
for n in range(len(line)):
    # print(sum(line[: n + 1]))
    result.append(sum(line[: n + 1]))

print(sum(result))
