from bisect import bisect_left, bisect_right

N = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(set(nums))

for num in nums:
        print(bisect_left(sorted_nums, num), end=' ')