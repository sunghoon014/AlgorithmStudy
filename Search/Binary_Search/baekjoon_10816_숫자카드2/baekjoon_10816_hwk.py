from bisect import bisect_left, bisect_right

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

M = int(input())
answer = [0]*M
for idx, num in enumerate(map(int, input().split())):
        left = bisect_left(nums, num)
        right = bisect_right(nums, num)
        if left!=right: answer[idx] += (right-left)

print(*answer)
