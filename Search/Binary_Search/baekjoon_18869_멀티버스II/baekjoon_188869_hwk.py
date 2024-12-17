from bisect import bisect_left, bisect_right
M, N = map(int, input().split())
all = [list(map(int, input().split())) for _ in range(M)]
idxs = []
for uni in all:
    pos = [0]*N
    sorted_uni = sorted(uni)
    for i in range(N):
        pos[i] = bisect_left(sorted_uni, uni[i])
    idxs.append(pos)

history = []
answer=0
for seq in idxs:
    if seq in history:
        continue
    cnt = idxs.count(seq)
    answer += cnt*(cnt-1)//2 if cnt>1 else 0
    history.append(seq)
print(answer)