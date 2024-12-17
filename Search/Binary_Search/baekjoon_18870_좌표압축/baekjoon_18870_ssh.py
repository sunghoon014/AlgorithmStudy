import sys
import bisect

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

X_sorted = sorted(list(set((X))))

res = []
for coord in X:
    res.append(bisect.bisect_left(X_sorted, coord))

print(' '.join(map(str, res)))