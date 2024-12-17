N = int(input())
nums = [int(input()) for _ in range(N)]
counts = {}
for num in nums:
    if counts.get(num):
        counts[num] += 1
    else:
        counts[num] = 1

counts = sorted(counts, key=lambda x:(-counts[x], x))
print(counts[0])