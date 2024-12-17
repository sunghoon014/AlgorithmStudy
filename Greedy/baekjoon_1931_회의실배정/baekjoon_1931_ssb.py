import sys
input = sys.stdin.readline
n = int(input())

table = []
for _ in range(n):
    i, j = map(int, input().split())
    table.append([i, j])

table = sorted(table, key=lambda x:(x[1], x[0]-x[1]))

start, end = table[0]
cnt = 1
for i in range(1, n):
    if table[i][0] >= end:
        cnt += 1
        start, end = table[i]

print(cnt)