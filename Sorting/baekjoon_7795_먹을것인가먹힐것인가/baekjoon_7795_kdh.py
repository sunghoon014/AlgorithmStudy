# 7795 먹을 것인가 먹힐 것인가
import bisect
T=int(input())
for _ in range(T):
    A_N,B_M=map(int,input().split())
    A_list=list(map(int,input().split()))
    B_list=list(map(int,input().split()))
    A_list.sort(reverse=True)
    B_list.sort()
    ans=0
    for A_fish in A_list:
        idx=bisect.bisect_left(B_list,A_fish)
        if idx==0:
            break
        ans+=idx
    print(ans)