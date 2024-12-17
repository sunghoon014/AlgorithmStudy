import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().strip().split()))

max_len = 0
p = [0] * (1000001)  # 1e6+1

for num in nums:
    p[num] = p[num-1] + 1
    max_len = max(max_len, p[num])

print(N - max_len)


# ans = 0
# tmp = []
# sort = []

# for i in range(N-1):
#     if nums[i] < nums[i+1]:
#         bisect.insort(sort, nums[i])
#         if tmp:
#             bisect.insort(sort, tmp[-1])
#             tmp.pop()
#             ans += 1
#     else:
#         tmp.append(nums[i])

# if nums[-1] not in sort:
#     ans += 1

# tmp = []
# for num in nums:
#     if not tmp or tmp[-1] < num:
#         tmp.append(num)
#     else:
#         tmp[bisect.bisect_left(tmp, num)] = num

# print(N - len(tmp))