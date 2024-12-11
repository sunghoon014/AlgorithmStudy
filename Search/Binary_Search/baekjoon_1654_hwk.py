# K개의 LAN선을 잘라서 일정한 길이의 LAN선을 N개 이상 만드는 것이 목표
# K개 LAN선에서 균일하게 n개씩 만든다고 생각할 때 최대 길이를 가지는 n의 범위는
# [K개의 LAN선 중 가장 작은 값 // n, K개의 LAN선 중 가장 큰 값 // n]이다.
# 그리고 이 범위에서 최대 길이를 가지는 n이 정답이 되고, 이를 이진탐색으로 구할 수 있음
K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]
lans.sort() # 최대, 최솟값 구하기 귀찮아서 정렬하고 인덱싱 할 것
mok = N//K if N%K==0 else N//K+1    # 균일하게 n개씩 그 n
start = max(1, lans[0]//mok) # 최소
end = lans[-1]//mok   # 최대
answer = 0

while start <= end:
    mid = (start+end)//2   # 탐색 지점
    if sum([num//mid for num in lans]) >= N:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)