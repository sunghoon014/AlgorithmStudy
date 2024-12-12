m, n = map(int, input().split())
data = list(map(int, input().split()))

left, right = 1, max(data)

if m > sum(data):
    print(0)
else:
    while left<=right:
        mid = (left+right)//2
        cnt = sum(map(lambda x: x//mid, data))
        if cnt < m:
            right = mid-1
        else:
            left = mid+1
    print(right)