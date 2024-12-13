# 이진 탐색
N = int(input())
liquids = sorted(map(int, input().split()))
min_value = abs(liquids[0]+liquids[-1])
answer = (liquids[0], liquids[-1])
for fix in range(N-1):
    start, end = fix+1, N-1
    while start <= end:
        mid = (start+end)//2
        ph = liquids[fix]+liquids[mid]
        if min_value > abs(ph): # 매번 저장하지 않고 최소값 갱신할 때만 저장
            min_value = abs(ph)
            answer = (liquids[fix], liquids[mid])
            if ph==0: break

        if ph > 0:
            end = mid - 1
        else:
            start = mid + 1
    if min_value==0: break  # 최소값이 0이면 더 보지 않고 바로 break
print(*answer)

# 투 포인터
N = int(input())
liquids = list(map(int, input().split()))
start, end = 0, N-1
value = abs(liquids[start] + liquids[end])
answer = (liquids[start], liquids[end])
while start < end:
    ph = liquids[start] + liquids[end]
    if value>abs(ph):   # 매 번 저장하지 않고 최소값 갱신할 때만 저장
        value = abs(ph)
        answer = (liquids[start], liquids[end])
        if value==0:
            break
    if ph>0:
        end-=1
    else:
        start+=1
print(*answer)