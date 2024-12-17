import sys

num_a, num_b = map(int, sys.stdin.readline().split())
A = map(int, sys.stdin.readline().split())
B = set(map(int, sys.stdin.readline().split()))

res = []
for num in A:
    if not num in B:
        res.append(num)

res.sort()

if (len(res) == 0):
    print(0)
else:
    print(len(res))
    print(' '.join(map(str, res)))
