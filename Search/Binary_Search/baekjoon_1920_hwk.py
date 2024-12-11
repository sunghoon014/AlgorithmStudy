from bisect import bisect_left, bisect_right

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
M = int(input())

for num in list(map(int, input().split())):
        if bisect_left(nums, num)==bisect_right(nums, num): print(0)
        else: print(1)