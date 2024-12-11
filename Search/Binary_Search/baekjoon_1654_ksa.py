import sys
K, N = map(int, sys.stdin.readline().split())
length = [int(sys.stdin.readline()) for _ in range(K)]

length.sort() #457 549 743 802

left = 1
right = max(length)

def binary_search(N, left, right):
    if left>right:
        return right
    
    mid = (left + right) // 2
    cnt = 0
    
    for i in length:
        cnt += i // mid
        
    if cnt == N:
        return binary_search(N, mid + 1, right)
    elif cnt > N:
        return binary_search(N, mid + 1, right)
    else: #cnt < N
        return binary_search(N, left, mid - 1)
    
output = binary_search(N, left, right)
print(output)