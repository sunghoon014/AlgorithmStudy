import sys

input = sys.stdin.readline

lst = list(map(str, input().split()))
n = int(lst.pop(0))

for _ in range(n - len(lst)):
    lst.extend(list(map(str, input().split())))

lst = [int(x[::-1]) for x in lst]
lst.sort()
for l in lst:
    print(l)
