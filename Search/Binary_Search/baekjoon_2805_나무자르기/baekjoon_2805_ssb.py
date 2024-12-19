n, m = map(int, input().split())
trees = list(map(int, input().split()))

left, right = 0, max(trees)

while left<=right:
    mid = (left+right)//2
    result = sum(map(lambda x: x-mid if x-mid>0 else 0, trees))
    if result<m:
        right = mid-1
    else:
        left = mid+1

print(right)