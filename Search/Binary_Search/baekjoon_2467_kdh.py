# 2467 용액
import bisect
N=int(input())
liquid_list=list(map(int,input().split()))
left_idx=0
right_idx=len(liquid_list)-1
result=[]
while left_idx<right_idx:
    if liquid_list[left_idx]+liquid_list[right_idx]<0:
        result.append([left_idx,right_idx,-(liquid_list[left_idx]+liquid_list[right_idx])])
        left_idx+=1
    else:
        result.append([left_idx,right_idx,liquid_list[left_idx]+liquid_list[right_idx]])
        right_idx-=1

result.sort(key=lambda x : x[2])
print(liquid_list[result[0][0]],liquid_list[result[0][1]])
