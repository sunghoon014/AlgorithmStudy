k, n = map(int, input().split())
data = [int(input()) for _ in range(k)]

left, right = 1, max(data)

cnt = 0
while left<=right:
    mid = (left+right)//2
    cnt = sum(map(lambda x: x//mid, data))
    if cnt<n:
        right = mid-1
    else:
        left = mid+1

print(right)