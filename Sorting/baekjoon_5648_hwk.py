nums = input().split()
n=int(nums.pop(0))-len(nums)

while n:
    inp = input().split()
    n-=len(inp)
    nums.extend(inp)
nums = [int(''.join(list(reversed(element)))) for element in nums]
nums.sort()
for e in nums: print(e)