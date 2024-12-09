import sys

input = sys.stdin.readline
n, k = map(int, input().split())
a_lst = [int(input()) for _ in range(n)][::-1]

count = 0
for a in a_lst:
    c, d = divmod(k, a)
    if c > 0:
        count += c
        k = d

print(count)
