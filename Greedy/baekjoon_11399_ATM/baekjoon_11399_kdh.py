# 11399 ATM
N=int(input())
time_list=list(map(int,input().split()))
time_list.sort()
result=0
temp_time=0
for cur_time in time_list:
    temp_time+=cur_time
    result+=temp_time

print(result)