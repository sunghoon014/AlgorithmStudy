# 18870 좌표압축
import bisect
N=int(input())
X_list=list(map(int,input().split()))
processed_X_list=list(set(X_list))
processed_X_list.sort()

# 1000 999 1000 999 1000 999
# [999 1000] 
result=[0]*N
for idx,X in enumerate(X_list):
    result[idx]=bisect.bisect(processed_X_list,X)-1

print(*result)