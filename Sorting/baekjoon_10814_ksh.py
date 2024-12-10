import sys

input = sys.stdin.readline

n = int(input())
result = [list(input().split()) for _ in range(n)]
result.sort(key=lambda x: int(x[0]))

for x in result:
    print(" ".join(x))
