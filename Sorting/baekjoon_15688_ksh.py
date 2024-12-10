import sys

input = sys.stdin.readline

n = int(input())
result = [int(input()) for _ in range(n)]
result.sort()

for x in result:
    print(x)
