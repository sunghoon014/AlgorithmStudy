N = int(input())
nums = [tuple(map(int, input().split())) for _ in range(N)]
nums.sort()
for f, s in nums:
	print(f, s)