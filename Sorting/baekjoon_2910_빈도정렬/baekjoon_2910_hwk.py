N, C = map(int, input().split())
nums = list(map(int, input().split()))
freq = {num:0 for num in list(set(nums))}   # 빈도
idxs = {}   # 나온 순서
for idx, num in enumerate(nums):
    freq[num] += 1
    if idxs.get(num)!=None: continue
    idxs[num] = idx

sorted_dict = sorted(freq.items(), key=lambda x:(-x[1], idxs[x[0]]))
for k, v in sorted_dict:
    for _ in range(v):
        print(k, end=" ")