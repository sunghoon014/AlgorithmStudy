import sys

M, N = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))

if sum(L) < M:
    print("0")
    sys.exit()

start, end = 1, max(L)
while start <= end:
    mid = (start + end) // 2
    total = 0
    
    for cookie in L:
        total += cookie // mid
    
    if total >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)