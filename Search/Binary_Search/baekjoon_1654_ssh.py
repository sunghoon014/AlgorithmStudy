import sys
K, N = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for lines in lan:
        total += lines // mid
    
    if total >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)