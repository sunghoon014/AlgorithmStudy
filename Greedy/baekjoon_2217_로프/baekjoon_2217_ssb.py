import sys
input = sys.stdin.readline
n = int(input())

data = [int(input()) for _ in range(n)]
data.sort(reverse=True)

lst = []
for i, j in enumerate(data):
    lst.append((i+1)*j)

print(max(lst))