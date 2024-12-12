# 1822 차집합
import bisect
N_A,N_B=map(int,input().split())
A_list=list(map(int,input().split()))
B_list=list(map(int,input().split()))
B_list.sort()
result=[]
for target_num in A_list:
    if B_list[bisect.bisect(B_list,target_num)-1]==target_num:
        continue
    else:
        result.append(target_num)

result.sort()
print(len(result))
print(*result)