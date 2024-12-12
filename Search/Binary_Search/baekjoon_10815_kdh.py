# 10815 숫자카드
import bisect
N=int(input())
N_list=list(map(int,input().split()))
M=int(input())
M_list=list(map(int,input().split()))

N_list.sort()

for target_num in M_list:
    if N_list[bisect.bisect(N_list,target_num)-1]==target_num:
        print(1,end=' ')
    else:
        print(0,end=' ')