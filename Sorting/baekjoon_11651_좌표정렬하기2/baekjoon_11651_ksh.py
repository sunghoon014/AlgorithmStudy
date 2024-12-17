import sys

input = sys.stdin.readline

n = int(input())
result = [list(map(int, input().split())) for _ in range(n)]
result.sort(key=lambda x: (x[1], x[0]))

for x in result:
    print(x[0], x[1])
