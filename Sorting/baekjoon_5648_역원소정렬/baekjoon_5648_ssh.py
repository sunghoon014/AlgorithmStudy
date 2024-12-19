import sys

input = sys.stdin.read
data = input().split()
N = int(data[0])

nums = []
for i in range (1, N + 1):
    num = int(data[i][::-1])
    nums.append(num)

nums.sort()

for num in nums:
    print(num)